from django.test import Client, TestCase
from django.test import SimpleTestCase
from django.urls import reverse

from django.contrib.auth import get_user_model

from .models import Trip, Destination, Hotel, Flight

# Create your tests here.


class TripTests(TestCase):



    def setUp(self):

        self.trip = Trip.objects.create(

            name="Mars",
            start_date="2022-5-5"

    )