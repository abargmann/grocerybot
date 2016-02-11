from __future__ import absolute_import
from django.conf import settings
from twilio.rest import TwilioRestClient

from .models import Produce

client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def send_sms_seasonal_produce(location, phone_number):
	"""Send a message with fruits in season for a location"""
	# Get our produce(s) from the database
	# produce = Produce.objects.filter(state__exact=location)[:5]
	produce_names = [p.name for p in Produce.objects.filter(state__exact=location)[:5]]
	# for p in produce:
	# 	name = produce.name
	# 	produce_list += name
	body = 'The following are in season for your state: ' + str(produce_names)

	message = client.messages.create(
		body=body,
		to=phone_number,
		from_=settings.TWILIO_NUMBER,
	)