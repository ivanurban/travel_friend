from django.db import models

from triplaner.models import Trip, Destination, Flight, Hotel #importing model from triplaner app

from django.conf import settings
# Create your models here.

class Profile(models.Model):
    #The user one-to-one field allows to associate profiles with users.
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'


  