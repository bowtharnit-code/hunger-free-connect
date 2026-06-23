from django.contrib import admin
from .models import FoodDonation, FoodRequest

admin.site.register(FoodDonation)
admin.site.register(FoodRequest)