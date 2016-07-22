from django.shortcuts import render, redirect
from .models import User,Trip
from django.core.urlresolvers import reverse
import re
import bcrypt
# Create your views here.

def index(request):
    context = {
     "users" : User.objects.all()
    }
    return render(request, 'travel/index.html', context)
    request.session['loggedin']=''

def create(request):

    if validate(request):
        User.objects.create(name=request.POST['name'],username=request.POST['username'],password=request.POST['password'])
        return redirect('/')
    else:
        print "invalid"
        return redirect('/')

def login(request):


    if request.session['loggedin'] == True:
        user = User.objects.get(id=request.session['user'])
        context={
            'users' : user,
            'trips' : Trip.objects.all().exclude(user=user),
            'usertrips':Trip.objects.filter(user=user)

        }

        return render(request, 'travel/travels.html', context)
    else:
        if len(User.objects.filter(username=request.POST['username']))==0:
            return render(request,'travel/index.html')
        else:
            user = User.objects.get(username=request.POST['username'])
            password = request.POST['password']
            ##make Session for user

            if user.password == password:
                request.session['user']=user.id
                context={
                    'users' : user,
                    'trips' : Trip.objects.all(),
                    'usertrips':Trip.objects.filter(user=user)

                }
                request.session['loggedin']=True
                return render(request, 'travel/travels.html', context)


def addtravel (request):
    # Trip.objects.create(destiantion=request.POST['destiantion'],description=request.POST['description'],password=req

    return render(request,'travel/addtravel.html')
def submittravel(request):
    user=User.objects.get(id=request.session['user'])
    Trip.objects.create(destination=request.POST['destination'],description=request.POST['description'],travel_from=request.POST['travel_from'],travel_to=request.POST['travel_to'],user=user)

    return redirect(reverse("my_home"))
def destination (request,id):

    trip=Trip.objects.get(id=id)
    ##person going to
    user= Trip.objects.filter(user=trip.user)
    creator=User.objects.get(id=trip.user.id)

    otheruser=Trip.objects.filter(user=trip.user).exclude(user=creator)
    context = {
        'trip':trip,
        'otherusers':otheruser
    }
    return render(request, 'travel/viewdestination.html', context)
    
def join (request,id):
    user=User.objects.get(id=request.session['user'])
    trip =Trip.objects.get(id=id)
    Trip.objects.create(destination=trip.destination,description=trip.description,travel_from=trip.travel_from,travel_to=trip.travel_to,user=user)


    return redirect(reverse("my_home"))
def logout (request):
    request.session.pop('user')
    request.session['loggedin'] = False
    return redirect('/')


def validate(request):
    #check email
    if len(request.POST['username'])<3:
        print "too short"
        return False

    # check firstname
    elif len(request.POST['name'])<3:
        return False
    # Check password
    elif len(request.POST['password'])<8:
        return False
    elif request.POST['password'] == '':
        print ('Password cannot be blank', 'passwordError')
        return False

    elif len(request.POST['password']) < 8:
        print('Password must be greater than 8 characters', 'passwordError')
        return False
    # check confirmation
    elif len(request.POST['conpassword']) < 8:
        print('Please confirm password', 'confirmPasswordError')
        return False
    elif request.POST['password'] != request.POST['conpassword']:
        print('Passwords do not match', 'confirmPasswordError')
        return False

    return True
