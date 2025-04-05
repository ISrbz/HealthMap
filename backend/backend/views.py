from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        body = json.loads(request.body)
        # Use request.POST for form data or request.body for JSON data
        username = body['username']  # Use .get() to avoid KeyError
        password = body['password']
        user = authenticate(request , username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
        # return JsonResponse({'username': username, 'password': password}, status=200)