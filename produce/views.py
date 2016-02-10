from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView
from django_twilio.decorators import twilio_view
from twilio.twiml import Response

from .forms import ProduceSubmitForm
from .models import Produce

class SeasonalView(generic.ListView):
	"""Returns a list of the produce that is in season for the current day."""
	template_name = 'produce/list.html'
	context_object_name = 'produce_list'

	def get_queryset(self):
		today = datetime.datetime.now()
		return Produce.objects.filter(season_start__lte=today, season_end__gte=today)

class ProduceDetailView(generic.DetailView):
	"""Shows users a single produce entry."""

	model = Produce
	template_name = 'produce/produce_detail.html'

class ProduceUpdateView(generic.UpdateView):
	"""Powers a form to edit existing Produces"""

	model = Produce
	template_name = 'produce/submit.html'
	fields = ['name', 'state', 'food_type', 'season_start', 'season_end']
	# This should be updated to be a message, using djangos message thing
	success_url = reverse_lazy('list')

class ProduceDeleteView(generic.DeleteView):
	"""Prompts user to confirm deletion of produce and then delete"""
	model = Produce
	success_url = reverse_lazy('list')


@twilio_view
def sms(request):
	"""Receive incoming SMS messages.  Return a generic response."""
	message_body = request.POST.get('Body', '')
	r = Response()
	return r

def submit_new_produce(request):
	"""Add a new produce to the database from the ProduceSubmitForm."""
	if request.method == "POST":
		form = ProduceSubmitForm(request.POST)
		if form.is_valid():
			produce = form.save(commit=False)
			produce.save()
			# This thanks page is useless, should be a success message:
			return HttpResponseRedirect('/produce/thanks/')
	else:
		form = ProduceSubmitForm()
	return render(request, 'produce/submit.html', {'form': form})