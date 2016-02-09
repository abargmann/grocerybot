from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class Produce(models.Model):
	STATES = (
		('Alabama', 'Alabama'),
		('Alaska', 'Alaska'),
		('Arizona', 'Arizona'),
		('Arkansas', 'Arkansas'),
		('California', 'California'),
		('Colorado', 'Colorado'),
		('Connecticut', 'Connecticut'),
		('Delaware', 'Delaware'),
		('Florida', 'Florida'),
		('Georgia', 'Georgia'),
		('Hawaii', 'Hawaii'),
		('Idaho', 'Idaho'),
		('Illinois', 'Illinois') ,
		('Indiana', 'Indiana'),
		('Iowa', 'Iowa'),
		('Kansas', 'Kansas'),
		('Kentucky', 'Kentucky'),
		('Louisiana', 'Louisiana'),
		('Maine', 'Maine'),
		('Maryland', 'Maryland'),
		('Massachusetts', 'Massachusetts'),
		('Michigan', 'Michigan'),
		('Minnesota', 'Minnesota'),
		('Mississippi', 'Mississippi'),
		('Missouri', 'Missouri'),
		('Montana', 'Montana') ,
		('Nebraska', 'Nebraska'),
		('Nevada', 'Nevada'),
		('New Hampshire', 'New Hampshire'),
		('New Jersey', 'New Jersey'),
		('New Mexico', 'New Mexico'),
		('New York', 'New York'),
		('North Carolina', 'North Carolina'),
		('North Dakota', 'North Dakota'),
		('Ohio', 'Ohio'),
		('Oklahoma', 'Oklahoma'),
		('Oregon', 'Oregon'),
		('Pennsylvania', 'Pennsylvania') ,
		('Rhode Island', 'Rhode Island'),
		('South Carolina', 'South Carolina'),
		('South Dakota', 'South Dakota'),
		('Tennessee', 'Tennessee'),
		('Texas', 'Texas'),
		('Utah', 'Utah'),
		('Vermont', 'Vermont'),
		('Virginia', 'Virginia'),
		('Washington', 'Washington'),
		('West Virginia', 'West Virginia'),
		('Wisconsin', 'Wisconsin'),
		('Wyoming', 'Wyoming'),

	)
	FOOD_TYPE = (
		('Vegetable', 'Vegetable'),
		('Fruit', 'Fruit'),
		('Protein', 'Protein'),
		('Other', 'Other'),
    )
	name = models.CharField(max_length=200)
	food_type = models.CharField(max_length = 300, choices=FOOD_TYPE)
	season_start = models.DateField(blank=True, null=True)
	season_end = models.DateField(blank=True, null=True)
	state = models.CharField(max_length = 300, choices=STATES, default='New York')
	def __str__(self):
		return self.name
