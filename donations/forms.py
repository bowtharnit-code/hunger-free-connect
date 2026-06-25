from django import forms
from .models import FoodDonation

class FoodDonationForm(forms.ModelForm):

    class Meta:
        model = FoodDonation
        fields = '__all__'

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description is None:
            return ''
        return description