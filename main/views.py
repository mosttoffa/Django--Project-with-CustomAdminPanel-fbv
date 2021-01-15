from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from manager.models import Manager



# Create your views here.


def home(request):

    sitename = "Amin Tech Ltd | Home"

    return render(request, 'front/home.html', {'sitename':sitename})



def panel(request):

    #Login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    #Login check end
    
    #user permission on panel
    perm = 0
    perms = Permission.objects.filter(user=request.user)
    for i in perms :
        if i.codename == "masteruser" : perm = 1
    
    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})


    return render(request, 'back/home.html')


def my_login(request):

    #Login authentication 
    if request.method == 'POST':
        utxt = request.POST.get('username')
        ptxt = request.POST.get('password')
              #User authentic
        if utxt != "" and ptxt !="":
            user = authenticate(username=utxt, password=ptxt)
                #If user does't exixt
            if user != None:
                login(request,user)
                return redirect('panel')

    return render(request, 'front/login.html')


def myregister(request):

    if request.method == 'POST':
        #User Registration.
        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if name == "" :
            msg = "Input Your Name"
            return render(request, 'front/msgbox.html', {'msg':msg})

        if password1 != password2 :
            msg = "Your Pass Didn't Match"
            return render(request, 'front/msgbox.html', {'msg':msg})

        #Strong password Algorithm.
        count1 = 0
        count2 = 0
        count3 = 0 
        count4 = 0

        for i in password1 :

            if i > "0" and i < "9" :
                count1 = 1
            if i > "A" and i < "Z" :
                count2 = 1
            if i > 'a' and i < 'z' :
                count3 = 1
            if i > "!" and i < "(" :
                count4 = 1

        if count1 == 0 or count2 == 0 or count3 == 0 or count4 == 0 :
            msg = "Your Pass Is Not Strong"
            return render(request, 'front/msgbox.html', {'msg':msg})

        if len(password1) < 8 :
            msg = "Your Pass Must Be 8 Character"
            return render(request, 'front/msgbox.html', {'msg':msg})
        
        #Check similar UserName and Email from database.
        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0 :

            user = User.objects.create_user(username=uname,email=email,password=password1)
            b = Manager(name=name,utxt=uname,email=email)
            b.save()

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


