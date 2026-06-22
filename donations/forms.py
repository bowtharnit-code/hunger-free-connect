from django import forms
from .models import FoodDonation

class FoodDonationForm(forms.ModelForm):
    class Meta:
        model = FoodDonation
        fields = ['food_name', 'quantity', 'donor_name', 'location', 'expiry_date']