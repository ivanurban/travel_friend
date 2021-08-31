from django import template

from django.shortcuts import  HttpResponseRedirect, redirect


#impoer form to use it in the tag
from ..forms import  ProfileEditForm

from triplaner.models import Flight, Hotel, Trip, Destination

#create a Library instance to register template tags in the Django template
register = template.Library()

from django.db.models import Sum #used to calculate prices

#inclusion tag take the budget from current user returns dictionary, which is then rendered on budget.html, which can be included in any page
#budget_tags.py -> def my_budget -> budget.html -> base.html
@register.inclusion_tag("useraccount/budget.html", takes_context=True)
def my_budget(context):

    request=context['request']
  
    if ProfileEditForm(instance=request.user.profile):
    
        form = ProfileEditForm(instance=request.user.profile)
        budget = form['budget'].value()

    if budget == None:
        budget = 0

    
    return {'budget':budget}
       

#inclusion tag for overall costs of user
@register.inclusion_tag("useraccount/cost.html", takes_context=True)
def my_cost(context):

        request=context['request']
        #fetching sum of all prices for specefic user, user enters prices for flights and hotels
        qs1 = Flight.objects.filter(destination__trip__user=request.user).aggregate(f_expenses=Sum('price')) 
        qs2 = Hotel.objects.filter(destination__trip__user=request.user).aggregate(h_expenses=Sum('price'))

    
        if qs1['f_expenses'] == None:
            qs1['f_expenses'] = 0
        if qs2['h_expenses'] == None:
            qs2['h_expenses'] = 0

        costs = qs1['f_expenses'] + qs2['h_expenses']

        return {'costs': costs }

    

