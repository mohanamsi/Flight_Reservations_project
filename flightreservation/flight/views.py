from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from flight.models import Flight,Reservation,Passenger
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from flight.serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
# Create your views here.


@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(depaturecity=request.data['depaturecity'],arrivalcity=request.data['arrivalcity'],dateofdepature=request.data['dateofdepature'])
    serializer = FlightSerializer(flights,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])

    passenger = Passenger()
    passenger.firstname = request.data["firstname"]
    passenger.lastname = request.data["lastname"]
    passenger.middlename = request.data["middlename"]
    passenger.email = request.data["email"]
    passenger.phone = request.data["phone"]
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    reservation.save()
    return Response(status=status.HTTP_201_CREATED)





def flight(request):
    return HttpResponse("Flight Services")


class FlightListView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PassengerListView(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class PassengerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationListView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationDetail(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

