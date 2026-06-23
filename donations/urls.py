from django.urls import path
from . import views

urlpatterns = [
    path('', views.donation_list, name='donation_list'),
    path('add/', views.add_donation, name='add_donation'),
    path('edit/<int:id>/', views.edit_donation, name='edit_donation'),
    path('delete/<int:id>/', views.delete_donation, name='delete donation'),
    path('request/<int:id>/', views.request_food, name='request_food'),
    path('ngo-dashboard/', views.ngo_dashboard, name='ngo_dashboard'),
    
    path('login/', views.user_login, name='login'),
]
