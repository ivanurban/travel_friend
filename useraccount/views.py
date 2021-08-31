from django.shortcuts import render, HttpResponseRedirect

from django.urls import reverse

from django.http import HttpResponse

# from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, ProfileEditForm

from django.contrib.auth.decorators import login_required

from triplaner.models import Trip, Destination, Flight, Hotel #importing model from triplaner app

from .models import Profile #importing model from useraccount app

# Create your views here.

#decorator is used to check whether the current user is authenticated


#these two  functions render
#templates that are used to display users budget and overall costs using custom inclusion tag, 
#these templates budget.html and cost.html are then included in base.html then included in base.html
def my_budget(request):
    return render(request, "useraccount/budget.html")

def my_cost(request):
    return render(request, "useraccount/cost.html")






@login_required
def dashboard(request):
    
    #section variable is used  to track the site's section that the user is browsing. 
    #Multiple views may correspond to the same section.
    #This is a simple way to define the section that each view corresponds to.

  

    all_trips = Trip.objects.filter(user=request.user)


    template_name = 'useraccount/dashboard.html'
    context = {
        'section' : 'dashboard', 
        'all_trips' : all_trips,

    }
   
    return render (request, template_name, context)


def register(request):
    template_name = 'useraccount/register.html'
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user object but dont save it now
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            # Create the user profile, when user is registerd the profile created is empty
            Profile.objects.create(user=new_user)


            return render(request,'useraccount/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request , template_name, {'form':form})



@login_required
def edit(request):
    template_name = 'useraccount/edit.html'
    if request.method == 'POST':
        #get budget field which is on the ProfileEditForm
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
        return HttpResponseRedirect(reverse('useraccount:dashboard'))

    else:
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request,  template_name, {'profile_form': profile_form})



   
