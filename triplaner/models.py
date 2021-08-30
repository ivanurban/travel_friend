from django.db import models
import datetime
from django.urls import reverse #used for get_absolut_url()
from django.contrib.auth.models import User 

from django.utils.text import slugify

from django.db.models import Sum #used to calculate prices

import random #for generating random string
import string #For generating random string

# Create your models here.


def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True) 
    start_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name


    # self.chars = string.ascii_letters + string.punctuation
    # self.size = 12


 
   

    #slugify is used to make slug out of entered name TO DO - make it add the date so it cannot by 
    #duplicated easily
    def save(self, *args, **kwargs):
        self.chars = string.ascii_letters + string.punctuation
        self.slug = slugify(self.name + random_string_generator(12,self.chars))
        print(self.slug)
        super(Trip, self).save(*args, **kwargs)



    def get_absolute_url(self):
        return reverse('useraccount:dashboard')


    @property 
    def get_all_costs(self):
        qs1 = Flight.objects.filter(destination__trip__user=self.user).aggregate(f_expenses=Sum('price'))
        
        qs2 = Hotel.objects.filter(destination__trip__user=self.user).aggregate(h_expenses=Sum('price'))

        if qs1['f_expenses'] == None:
            qs1['f_expenses'] = 0
        if qs2['h_expenses'] == None:
            qs2['h_expenses'] = 0

        return qs1['f_expenses'] + qs2['h_expenses']


      
class Destination(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.location


    #get hotels fk destinations
    @property
    def get_hotel(self):
        return Hotel.objects.filter(destination=self.id)


    #get flights fk destinations
    @property
    def get_flight(self):
        return Flight.objects.filter(destination=self.id)



    #taking the costs for hotel and flight by foreign key from destination
    #using aggregate to sum prices and then cheking if querysets are None
    #and assigning them zero so they could add, returning qs1 qnd qs2 by dict keys
    @property
    def get_costs_by_location(self):

        qs1 = Flight.objects.filter(destination=self.id).aggregate(flight_expenses=Sum('price'))
        qs2 = Hotel.objects.filter(destination=self.id).aggregate(hotel_expenses=Sum('price'))
        if qs1['flight_expenses'] == None:
            qs1['flight_expenses'] = 0
        if qs2['hotel_expenses'] == None:
            qs2['hotel_expenses'] = 0

        return qs1['flight_expenses'] + qs2['hotel_expenses']

          
    @property 
    def get_costs_by_trip(self):
        qs3 = Flight.objects.filter(destination__trip=self.trip).aggregate(f_expenses=Sum('price'))
        
        qs4 = Hotel.objects.filter(destination__trip=self.trip).aggregate(h_expenses=Sum('price'))
        if qs3['f_expenses'] == None:
            qs3['f_expenses'] = 0
        if qs4['h_expenses'] == None:
            qs4['h_expenses'] = 0

        return qs3['f_expenses'] + qs4['h_expenses']
  
class Flight(models.Model):

    from_destination = models.CharField(max_length=100, blank=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.destination)



class Hotel(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    check_in_date = models.DateTimeField(blank=True)
    check_out_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name



   

