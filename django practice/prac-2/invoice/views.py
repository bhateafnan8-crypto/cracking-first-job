from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Second program Home Page")

def about(request):
    return HttpResponse("About Page")

def portfolio(request):
    return HttpResponse("Porfolio Page")