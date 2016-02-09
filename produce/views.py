from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django_twilio.decorators import twilio_view
from twilio.twiml import Response

from .forms import ProduceSubmitForm
from .models import Produce

@twilio_view
def sms(request):
	"""Receive incoming SMS messages.  Return a generic response."""
	# message_body = request.POST.get('Body', '')
	r = Resonse()
	r.message('Test')
	return r

def submit_new_produce(request):
	"""Add a new produce to the database via the web form."""
	if request.method == "POST":
		form = ProduceSubmitForm(request.POST)
		if form.is_valid():
			produce = form.save(commit=False)
			produce.save()
			return HttpResponseRedirect('/produce/thanks/')
	else:
		form = ProduceSubmitForm()
	return render(request, 'produce/submit.html', {'form': form})

