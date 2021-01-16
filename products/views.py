from django.shortcuts import render, get_object_or_404, redirect
from .models import  Categori, Products
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
import csv
from django.http import HttpResponse


# Create your views here.





def product_show(request, category_slug=None):

    category_page = None
    products = None
    
    if category_slug != None:
        category_page = get_object_or_404(Categori, slug=category_slug)
        products = Products.objects.filter(category=category_page, available=True)
  
    else: 
        products = Products.objects.all().filter(available=True)


    return render(request, 'front/product.html', { 'category': category_page, 'products': products})




def product_page(request):


    return render(request, 'front/product_detail.html')



def product_add(request):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    return render(request, 'back/product_add.html')



def export_product_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title','Category','price','stock','available', 'image', 'description'])
    for i in Products.objects.all() :
        writer.writerow([i.name, i.category, i.price, i.stock, i.available, i.image, i.description])


    return response



def import_product_csv(request):

    if request.method == 'POST' :

        csv_file = request.FILES['csv_file']

        if not csv_file.name.endswith('.csv'):
            error = "Please Input Csv File"
            return render(request, 'back/error.html' , {'error':error})

        if csv_file.multiple_chunks():
            error = "File Too Large"
            return render(request, 'back/error.html' , {'error':error})

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")

        for line in lines :

            fields =line.split(",")

            try:

                if len(Products.objects.filter(name=fields[0])) == 0 and fields[0] != "Title" and fields[0] != "" :
                    b = Products(name=fields[0])
                    b.save()
               
            except:
                print("finish")

    return redirect('product_list')

    # return render(request, 'back/product_add.html')




def product_list(request):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    products = Products.objects.all()

    return render(request, 'back/product_list.html', {'products':products})



