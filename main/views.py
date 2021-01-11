from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from django.contrib.auth import authenticate, login, logout

# Create your views here.



def home(request):

    sitename = "Amin Tech Ltd | Home"

    return render(request, 'front/home.html', {'sitename':sitename})



def panel(request):

    #Login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    #Login check end

    return render(request, 'back/home.html')


def my_login(request):

    #Login authentication
    if request.method == 'POST':
        utxt = request.POST.get('username')
        ptxt = request.POST.get('password')
              #user authentic
        if utxt != "" and ptxt !="":
            user = authenticate(username=utxt, password=ptxt)
                #user does't exixt
            if user != None:
                login(request,user)
                return redirect('panel')

    return render(request, 'front/login.html')

def my_logout(request):

    logout(request)
    
    return redirect('my_login')



def contact(request):

    return render(request, 'front/contact.html')



def product(request):

    sitename = "Amin Tech Ltd | Product"

    return render(request, 'front/product.html', {'sitename':sitename})


def product_detail(request):

    sitename = "Amin Tech Ltd | Product Details"

    return render(request, 'front/product_detail.html', {'sitename':sitename})


