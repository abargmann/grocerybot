import requests
import json

def get_markets_by_zip(zipcode):
	response = requests.get("http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip="
		+ zipcode)
	if response.status_code != requests.codes.ok:
		raise ApiError('Response: '.format(response.status_code))
	else:
		json_data = json.loads(response.text)
		# results = json_data['results']
		for i in json_data['results']:
			print i['marketname']

user_input = raw_input("Some input please: ")
get_markets_by_zip(user_input)