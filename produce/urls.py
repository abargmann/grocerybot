from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from . import views

app_name = 'produce'

urlpatterns = [
	# Inbound SMS view:
	url(r'^sms/$', views.sms, name='sms'),

	# List and Detail Views:
	url(r'^list/', views.SeasonalView.as_view(), name='list'),
	url(r'^(?P<pk>[0-9]+)/$', views.ProduceDetailView.as_view(), name='produce_detail'),

	# CRUD for Produce Items:
	url(r'^submit/', views.submit_new_produce, name='submit'),
	url(r'^thanks/', TemplateView.as_view(template_name='produce/thanks.html')),
	url(r'^(?P<pk>[0-9]+)/edit/$', views.ProduceUpdateView.as_view(), name='produce_edit'),
	url(r'^(?P<pk>[0-9]+)/delete/$', views.ProduceDeleteView.as_view(), name='produce_delete'),
]