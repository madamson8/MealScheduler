from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from api.models import User, Food
from django.contrib.auth import authenticate, login, logout
import json


# Create your views here.
def register(request):
    if request.method == "POST":
        if request.POST.get('password', '') == request.POST.get('v_password', ''):
            try:
                u = User()
                u.username = request.POST.get('email', '')
                u.set_password(request.POST.get('password', ''))
                u.save()
                user = authenticate(request, username = request.POST.get('email', ''), password=request.POST.get('password', ''))
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse(500, 'Server Error')
            except:
                return HttpResponse(500, 'Server Error')
        else:
            return HttpResponse(400, 'Bad request')
    else:
        return HttpResponse(405, 'Method not allowed')

def login_view(request):
    if request.method == "POST":
        user = request.POST.get('email', '')
        passw = request.POST.get('password', '')
        user = authenticate(request, username=user, password=passw)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('login?failure=400')
    else:
        return HttpResponse(405, 'Method not allowed')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def create_food(request):
    if request.method == "POST":
        processed_data = json.loads(request.body)
        try:
            f = Food()
            f.name = processed_data['name']
            f.calories = processed_data['calories']
            f.fat = processed_data['fat']
            f.protein = processed_data['protein']
            u = User.objects.get(id=processed_data['rel_user'])
            f.rel_user = u
            f.save()
            return HttpResponse(201, '201 CREATED')
        except:
            return HttpResponse(400, 'BAD REQUEST')
    else:
        return HttpResponse(405, 'Method not allowed.')

def get_food(request):
    if request.method == "GET":
        pass
    else:
        return HttpResponse(405, 'Method not allowed.')