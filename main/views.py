from django.shortcuts import render, get_object_or_404, redirect
from .models import Main


# Create your views here.


def home(request):

    sitename = "Amin Tech Ltd | Home"

    return render(request, 'front/home.html', {'sitename':sitename})


def contact(request):

    sitename = "Amin Tech Ltd | Contact"

    return render(request, 'front/contact.html', {'sitename':sitename})


def product(request):

    sitename = "Amin Tech Ltd | Product"

    return render(request, 'front/product.html', {'sitename':sitename})


def product_detail(request):

    sitename = "Amin Tech Ltd | Product Details"

    return render(request, 'front/product_detail.html', {'sitename':sitename})


def panel(request):


        return render(request, 'back/home.html')

