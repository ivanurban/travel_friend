from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect

from .models import Trip, Destination, Hotel, Flight

from django.contrib.auth.decorators import login_required #import za login_required decorator

from .forms import TripAddModelForm, DestinationAddModelForm, HotelAddModelForm, FlightAddModelForm


from django.urls import reverse, reverse_lazy

from useraccount.forms import  ProfileEditForm

from django.db.models import Sum #used to calculate prices


######CREATE######

# #Adding new Trip
@login_required
def trip_add(request):
    #get data from the form
    form = TripAddModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        # save the data from the form and
        obj.save()
        #reset form
        form = TripAddModelForm()
   
        return HttpResponseRedirect(reverse('useraccount:dashboard'))
        
    template_name = "triplaner/tripadd.html"
    context = {'form': form}
    return render(request, template_name, context)



#Adding new locations for Trip
@login_required
def location_add(request, pk):
  
    trip = Trip.objects.get(pk=pk)
    form = DestinationAddModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.trip = trip
        obj.save()
        form = DestinationAddModelForm()
       
        return HttpResponseRedirect(reverse('triplaner:location', args=(pk,)))
       
    template_name = "triplaner/locationadd.html"
    context = {'form': form}
    return render(request, template_name, context)


#Adding Hotel for location
@login_required
def hotel_add(request, pk):
    
    destination = Destination.objects.get(pk=pk)
    tripid = destination.trip_id

    form = HotelAddModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.destination = destination
        obj.save()
        form=HotelAddModelForm()
        
        return HttpResponseRedirect(reverse('triplaner:location', args=(tripid,)))
     
    template_name="triplaner/hoteladd.html"
    #passing form and passing specific destination based on pk 
    context={'form':form, 'destination': destination}
    return render(request, template_name, context)


#Adding Flights 
@login_required
def flight_add(request,pk):

    destination = Destination.objects.get(pk=pk)
    tripid = destination.trip_id

    form = FlightAddModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.destination = destination
        obj.save()
        form = FlightAddModelForm()
        return HttpResponseRedirect(reverse('triplaner:location', args=(tripid,)))
    template_name = "triplaner/flightadd.html"
    context={'form':form }
    return render(request, template_name, context) 


######READ######

#pk of Trip from url on dashboard.html page
@login_required
def location(request, pk):
    

    if ProfileEditForm(instance=request.user.profile):
    
        form = ProfileEditForm(instance=request.user.profile)
        budget = form['budget'].value()

    user = request.user
    #get trip based on the passed pk
    trip = Trip.objects.get(id=pk)

    #get hotel based on destination foreign key
    hotel = Hotel.objects.all()
    #get all locations based on that trips foreign key
    locations = Destination.objects.filter(trip=trip)

    flight = Flight.objects.all()


    template_name =  'triplaner/location.html'
    context = {'locations':locations, 'trip': trip, 'user':user,
    'hotel':hotel, 'flight':flight, 'budget':budget }
    return render(request, template_name, context )


######UPDATE######
@login_required
def trip_edit(request, pk):
    # fetch the object related to passed id
    
    obj = get_object_or_404(Trip, pk=pk)
    # pass the object as instance in form
    form = TripAddModelForm(request.POST or None, instance=obj)

    # save the data from the form and
    if form.is_valid():
        form.save()
        form = TripAddModelForm()
        return HttpResponseRedirect("/useraccount")
    template_name = "triplaner/tripedit.html"
    context = {'form': form }
    return render(request, template_name, context)




def location_edit(request,pk):
    # fetch the object related to passed id
    obj = get_object_or_404(Destination, pk=pk)
    
    tripid = obj.trip_id
  
    # pass the object as instance in form
    form = DestinationAddModelForm(request.POST or None, instance=obj)
    # save the data from the form and
    if form.is_valid():
        form.save()
        form = DestinationAddModelForm()
        return HttpResponseRedirect(reverse('triplaner:location', args=(tripid,)))
    template_name = "triplaner/locationedit.html"
    context = {'form': form }
    return render(request, template_name, context)

def hotel_edit(request,pk):

    # fetch the object Hotel related to passed id
    obj = get_object_or_404(Hotel, pk=pk)
    obj2 = get_object_or_404(Destination, pk=obj.destination_id)
    tripid = obj2.trip_id
    
    # pass the object as instance in form
    form = HotelAddModelForm(request.POST or None, instance=obj)

    # save the data from the form and
    if form.is_valid():
        form.save()
        form = HotelAddModelForm()
        return HttpResponseRedirect(reverse('triplaner:location', args=(tripid,)))
    template_name = "triplaner/hoteledit.html"
    context = {'form': form }
    return render(request, template_name, context)

def flight_edit(request, pk):
    # fetch the object related to passed id
    obj = get_object_or_404(Flight, pk=pk)
    obj2 = get_object_or_404(Destination, pk=obj.destination_id)
    tripid = obj2.trip_id

    
    #tripid = get_tripid_for_hotel_flights(obj)
    
    # pass the object as instance in form
    form = FlightAddModelForm(request.POST or None, instance=obj)

    # save the data from the form and
    if form.is_valid():
        form.save()
        form = FlightAddModelForm()
        return HttpResponseRedirect(reverse('triplaner:location', args=(tripid,)))
    template_name = "triplaner/flightedit.html"
    context = {'form': form }
    return render(request, template_name, context)

######DELETE######

def trip_delete(request, pk):
    # fetch the object related to passed id
    obj = get_object_or_404(Trip, pk=pk)
    if request.method=='POST':
        #delete object
        obj.delete()
        #redirect on profile page
        return HttpResponseRedirect("/useraccount")

    template_name="triplaner/tripdelete.html"
    context={}
    return render(request, template_name, context)

def location_delete(request, pk):
    # fetch the object related to passed id
    obj = get_object_or_404(Destination, pk=pk)
    tripid = obj.trip_id
   
    if request.method=='POST':
        #delete object
        obj.delete()
        #redirect on location page page
        return HttpResponseRedirect(reverse('triplaner:location', args=(tripid,)))

    template_name="triplaner/locationdelete.html"
    context={}
    return render(request, template_name, context) 

def hotel_delete(request, pk):
    # fetch the object related to passed id
    obj = get_object_or_404(Hotel, pk=pk)
    obj2 = get_object_or_404(Destination, pk=obj.destination_id)
    tripid = obj2.trip_id

    if request.method=='POST':
        #delete object
        obj.delete()
       
        return HttpResponseRedirect(reverse('triplaner:location', args=(tripid,)))

    template_name="triplaner/hoteldelete.html"
    context={}
    return render(request, template_name, context)   

def flight_delete(request, pk):
    # fetch the object related to passed id
    obj = get_object_or_404(Flight, pk=pk)
    obj2 = get_object_or_404(Destination, pk=obj.destination_id)
    tripid = obj2.trip_id

    if request.method=='POST':
        #delete object
        obj.delete()
        #redirect on profile page
        return HttpResponseRedirect(reverse('triplaner:location', args=(tripid,)))

    template_name="triplaner/flightdelete.html"
    context={}
    return render(request, template_name, context)   







    


 