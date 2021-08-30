from django.contrib import admin


from .models import Trip, Destination, Flight, Hotel
# Register your models here.

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display=('user','name','start_date','slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
     list_display=('trip','location')

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
     list_display=('from_destination','destination','date_time','price')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
     list_display=('destination','name','price')