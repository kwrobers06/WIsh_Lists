from django.shortcuts import render, HttpResponse, redirect
from ..login_reg.models import User
from .models import Item 

from django.contrib import messages

def dashboard(request):
    
    wished_4_items = User.objects.get(id=request.session['userid']).wishing_for.all()
    all_items = Item.objects.all()

    i1 = set(wished_4_items)
    i2 = set(all_items)
    
    i2 -= i1

    context = {
        "wishlist_items": i1,
        "not_wished_yet": i2

    }
    
    return render(request, 'item/dashboard.html', context)

def create(request):
    return render(request, 'item/create.html')

def logout(request):
    request.session.flush()
    return redirect('/')
def home(request):
    return redirect('/wish_items/dashboard')


def add(request):
    Item.objects.creator(request.POST['item'], request.session['userid'])
    return redirect ('/wish_items/dashboard')

def add_to_wishlist(request, item_id):
    Item.objects.add_to_wishlist(request.session['userid'], item_id)
    return redirect ('/wish_items/dashboard')

def remove_from_wishlist(request, item_id):
    Item.objects.remove_from_wishlist(request.session['userid'], item_id)
    return redirect ('/wish_items/dashboard')
def show_item(request,item_id):
    context = {
        "users_wished_by": Item.objects.get(id=item_id)
        }
    return render(request, 'item/show.html', context)
def delete(request, item_id):

    Item.objects.get(id=item_id).delete()
    return redirect ('/wish_items/dashboard')