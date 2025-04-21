#Connections to the user db

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        body = json.loads(request.body)
        # Use request.POST for form data or request.body for JSON data
        username = body['username']
        password = body['password']
        user = authenticate(request , username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid username or password'}, status=401)


@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        print(request.POST)
        logout(request)
        return JsonResponse({'message':'Successfuly logged out'})


@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        print(request.POST)
        body = json.loads(request.body)
        # Use request.POST for form data or request.body for JSON data
        username = body['username']
        password = body['password']
        user = authenticate(request , username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            if User.objects.filter(username=username).exists():
                return JsonResponse({'message':'Username already exists'}, status=409)
            
            new_user = User.objects.create_user(username=username, email=None, password=password)
            login(request, new_user)
            return JsonResponse({'message': 'Login successful'})