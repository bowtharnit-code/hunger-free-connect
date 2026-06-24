from django.shortcuts import render, redirect
from .forms import FoodDonationForm
from .models import FoodDonation, FoodRequest

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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

def ngo_dashboard(request):
    total_donations = FoodDonation.objects.count()
    total_requests = FoodRequest.objects.count()

    pending_requests = FoodRequest.objects.filter(
        status="Pending"
    ).count()

    recent_donations = FoodDonation.objects.order_by('-id')[:5]

    context = {
        'total_donations': total_donations,
        'total_requests': total_requests,
        'pending_requests': pending_requests,
        'recent_donations': recent_donations,
    }

    return render(request, 'donations/ngo_dashbo"ard.html', context)

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect("/")

    return render(request, "donations/login.html")

def user_logout(request):
    logout(request)
    return redirect("/login/")

def signup(request):
    if request.method == "POST":
        print("POST received")
        return redirect("/login/")

    return render(request, "donations/signup.html")