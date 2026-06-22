from django.db import models

class FoodDonation(models.Model):
    food_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    donor_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    expiry_date = models.DateField()
    status = models.CharField(max_length=20, default="Available")

    def __str__(self):
        return self.food_name
