from django	import forms

from .models import	Produce

class ProduceSubmitForm(forms.ModelForm):
	class Meta:
		model = Produce
		fields = ('name', 'food_type', 'season_start', 'season_end')