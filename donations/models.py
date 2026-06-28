from django.db import models
from django.contrib.auth.models import User

class FoodDonation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    food_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    donor_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    expiry_date = models.DateField()
    
    food_image =models.ImageField(upload_to='food_images/', blank=True, null=True)
    
    food_type = models.CharField(max_length=50, default="Veg")

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    receiver_name = models.CharField(max_length=100, blank=True)

    receiver_phone = models.CharField(max_length=15, blank=True)

    STATUS_CHOICES = [
        ("Available", "Available"),
        ("Requested", "Requested"),
        ("Collected", "Collected"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Available"
    )

    def __str__(self):
        return self.food_name


class FoodRequest(models.Model):
    requester_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    food_needed = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.requester_name