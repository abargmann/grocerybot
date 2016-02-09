from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from produce import views

app_name = 'produce'

urlpatterns = [
	url(r'^sms/$', 'produce.views.sms'),
	url(r'^submit/', views.submit_new_produce, name='submit'),
	url(r'^thanks/', TemplateView.as_view(template_name='produce/thanks.html')),
]