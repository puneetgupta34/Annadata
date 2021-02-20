from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Crop , Front
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
    dest = Crop.objects.all()
    obj = Front.objects.all()
    return render(request, 'index.html', {'dests' : dest, 'front' : obj})


def logout(request):
    auth.logout(request)
    return redirect('/')  