from django.shortcuts import render, get_object_or_404, redirect
from .models import Manager
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.


def manager_list(request):


    return render(request, 'back/manager_list.html')
