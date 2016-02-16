import requests
import json

def get_markets_by_zip(zipcode):
	response = requests.get("http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip="
		+ zipcode)
	json_data = json.loads(response.text)
	# results = json_data['results']
	for i in json_data['results']:
		print i['marketname']

