from django.http import HttpResponse, JsonResponse,HttpResponseBadRequest
from django.shortcuts import render,redirect

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contact.html')

def home(request):
    return render(request, 'Homepage.html')

def service(request):
    return render(request, 'Services.html')

def login(request):
    return render(request, 'login.html')
