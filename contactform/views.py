from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactForm
from django.contrib.auth import authenticate, login, logout
import datetime

# Create your views here.


def contact_add(request):

    #create date & time 
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    
    if len(str(day)) == 1 :
        day = "0" + str(day)
    if len(str(month)) == 1 :
        month = "0" + str(month)
 
    today = str(year) + "/" + str(month) + "/" + str(day)
    time = str(now.hour) + ":" + str(now.minute)
    #End date & time section
    
    # create contact details # creating objects and save
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        txt = request.POST.get('msg')

        if name == "" or email == "" or txt == "" :
            msg = "All Fields Requirded"
            return render(request, 'front/msgbox.html', {'msg':msg})
        
        b = ContactForm(name=name,email=email,txt=txt,date=today,time=time)
        b.save()
        msg = "Your Message Received."
        return render(request, 'front/msgbox.html', {'msg':msg})

    return render(request, 'front/msgbox.html')



def contact_show(request):

     #Login check start
    if not request.user.is_authenticated:
        return redirect('my_login')
    #Login check end
    
    # retrive all objects
    msg = ContactForm.objects.all()

    return render(request, 'back/contact_form.html', {'msg':msg})



def contact_del(request, pk):

    # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    
    # delete through PK
    b = ContactForm.objects.filter(pk=pk)
    b.delete()

    return redirect('contact_show')
