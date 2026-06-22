from django.shortcuts import render, redirect
from .models import FoodDonation
from .forms import FoodDonationForm


def donation_list(request):
    search = request.GET.get('search')

    if search:
        donations = FoodDonation.objects.filter(location__icontains=search)
    else:
        donations = FoodDonation.objects.all()

    return render(request, 'donations/list.html', {
        'donations': donations
    })


def add_donation(request):
    if request.method == 'POST':
        form = FoodDonationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FoodDonationForm()

    return render(request, 'donations/add_donation.html', {
        'form': form
    })


def edit_donation(request, id):
    donation = FoodDonation.objects.get(id=id)

    if request.method == 'POST':
        form = FoodDonationForm(request.POST, instance=donation)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FoodDonationForm(instance=donation)

    return render(request, 'donations/add_donation.html', {
        'form': form
    })


def delete_donation(request, id):
    donation = FoodDonation.objects.get(id=id)
    donation.delete()
    messages.success(request, "Donation delete successfully!")
    return redirect('/') 

def request_food(request, id):
    donation = FoodDonation.objects.get(id=id)
    donation.status = "Requested"
    donation.save()

    return redirect('/')