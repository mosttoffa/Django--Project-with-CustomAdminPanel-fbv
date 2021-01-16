from django.shortcuts import render, get_object_or_404, redirect
from .models import Products, Categori

# Create your views here.





def product_page(request):


    return render(request, 'front/product_detail.html')
