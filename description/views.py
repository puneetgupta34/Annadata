
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def contact(request):
     return render(request,'contact.html')

def about(request):
    return render(request,'about.html')