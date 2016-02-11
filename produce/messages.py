from __future__ import absolute_import
from django.conf import settings
from twilio.rest import TwilioRestClient

from .models import Produce

client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def send_sms_seasonal_produce(location, phone_number):
	"""Send a message with fruits in season for a location"""
	# Get our produce(s) from the database
	produce_names = [p.name for p in Produce.objects.filter(state__exact=location)[:5]]
	body = 'The following are in season for your state: ' + str(produce_names)

	# Should probably use a TwilioMessages class or
	# something and have methods for respond and send
	# rather thanr repeating this in every one...
	message = client.messages.create(
		body=body,
		to=phone_number,
		from_=settings.TWILIO_NUMBER,
	)

def send_sms_produce_detail(produce_name, phone_number):
	"""Send a message with the basic information about a specific entry"""
	produce = Produce.objects.filter(name__exact=produce_name)[:5]
	if len(produce) > 0:
		for p in produce:
			# Probably don't want to send a message for each one (that's a lot)
			# But can test with this for now
			message = client.messages.create(
				body=p.name + " is in season from " + str(p.season_start) + " to " + str(p.season_end) + " in " + p.state,
				to=phone_number,
				from_=settings.TWILIO_NUMBER,
			)
	else:
		message = client.messages.create(
			body="No produce found!",
			to=phone_number,
			from_=settings.TWILIO_NUMBER,
		)

