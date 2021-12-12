from django.db import models

# Create your models here.
class Flight(models.Model):
    flightnumber = models.CharField(db_column='flightNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    operatingairlines = models.CharField(db_column='operatingAirlines', max_length=255, blank=True, null=True)  # Field name made lowercase.
    depaturecity = models.CharField(db_column='depatureCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    arrivalcity = models.CharField(db_column='arrivalCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateofdepature = models.DateField(db_column='dateOfDepature', blank=True, null=True)  # Field name made lowercase.
    estimatedtimeofdepatur = models.TimeField(db_column='estimatedTimeOfDepatur', blank=True, null=True)  # Field name made lowercase.

    # def __str__(self):
    #     return f"{self.flightnumber}"


class Passenger(models.Model):
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='middleName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.

    # def __str__(self):
    #     return f"{self.firstname} {self.lastname}"

class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)