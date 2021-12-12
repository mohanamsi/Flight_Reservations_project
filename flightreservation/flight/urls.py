from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.flight),
    path('findflights/',views.find_flights),
    path('flightslist/',views.FlightListView.as_view()),
    path('flights/<int:pk>/',views.FlightDetail.as_view()),
    path('passengers/',views.PassengerListView.as_view()),
    path('passengers/<int:pk>/',views.PassengerDetail.as_view()),
    path('reservation/',views.ReservationListView.as_view()),
    path('reservation/<int:pk>/',views.ReservationDetail.as_view()),
    path('savereservation/',views.save_reservation),
    path('token/',obtain_auth_token),
]