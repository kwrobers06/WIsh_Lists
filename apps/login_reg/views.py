from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from .models import User
from ..item.models import Item
from django.contrib import messages
# index -> '/'
def index(request):
    # User.objects.all().delete()
    return render (request, 'login_reg/index.html')

# register ->'/register$'
def register(request):
    result = User.objects.validate(request.POST)
    if result['status'] == True:
        user = User.objects.creator(request.POST)
        messages.success(request,'User has been created')
    else:
        for error in result['errors']:
            messages.error(request,error)
    return redirect ('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results ['status']==False:
        messages.error(request, "Check your password and user name")
        return redirect ('/')
    request.session['user_name']=results['user'].user_name
    request.session['first_name']=results['user'].first_name
    request.session['userid'] = results['user'].id
    return redirect('/wish_items/dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')

def add(request):
    print "HHHHEEEELLLOOOOO**********"
    result = Item.objects.validate(request.POST)
    if result['status'] == True:
        item=Item.objects.create_item(request.POST,request.session['user_name'])
        messages.success(request,'Item has been created')
    else:
        for error in result['errors']:
            messages.error(request,error)

    
    return redirect ('item/create.html')

    
    




# Create your views here.
