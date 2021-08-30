from django.urls import path, include

 #to use with Class-based Views

from . import views

app_name = 'triplaner'


urlpatterns = [


    # path('', include('django.contrib.auth.urls')),

    #read
    path('location/<int:pk>/', views.location, name='location'),


    #create
    path('tripadd/', views.trip_add, name='tripadd'),

    path('locationadd/<int:pk>/', views.location_add, name='locationadd'),

    path('hoteladd/<int:pk>/', views.hotel_add, name='hoteladd'),

    path('flightadd/<int:pk>/', views.flight_add, name='flightadd'),

    #update
    path('tripedit/<int:pk>/', views.trip_edit, name='tripedit'),

    path('locationedit/<int:pk>/', views.location_edit, name='locationedit'),


    path('hoteledit/<int:pk>/', views.hotel_edit, name='hoteledit'),

    path('flightedit/<int:pk>/', views.flight_edit, name='flightedit'),

    #delete
    path('tripdelete/<int:pk>/', views.trip_delete, name='tripdelete'),


    path('locationdelete/<int:pk>/', views.location_delete, name='locationdelete'),

    path('hoteldelete/<int:pk>/', views.hotel_delete, name='hoteldelete'),

    path('flightdelete/<int:pk>/', views.flight_delete, name='flightdelete'),




]