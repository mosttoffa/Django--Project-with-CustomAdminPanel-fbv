from django.shortcuts import render, get_object_or_404, redirect
from .models import Manager
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission


# Create your views here.


def manager_list(request):

    
    manager = Manager.objects.all()

    return render(request, 'back/manager_list.html', {'manager':manager})



def manager_del(request,pk):


    manager = Manager.objects.get(pk=pk)
    b = User.objects.filter(username=manager.utxt)
    b.delete()

    manager.delete()

    return redirect('manager_list')


def manager_group(request):

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    group = Group.objects.all().exclude(name="masteruser")

    return render(request, 'back/manager_group.html', {'group':group})



def manager_group_add(request):


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})


    if request.method == 'POST' :

        name = request.POST.get('name')

        if name != "" :

            if len(Group.objects.filter(name=name)) == 0 :

                group = Group(name=name)
                group.save()

    return redirect('manager_group')



def manager_group_del(request, name):


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})


    b = Group.objects.filter(name=name)
    b.delete()


    return redirect('manager_group')



def users_groups(request,pk):

    
    manager = Manager.objects.get(pk=pk)

    user = User.objects.get(username=manager.utxt)

    ugroup = []
    for i in user.groups.all():
        ugroup.append(i.name)
    
    group = Group.objects.all()

    return render(request, 'back/users_groups.html', {'ugroup':ugroup, 'group':group, 'pk':pk})



def add_users_to_groups(request,pk):


    if request.method == 'POST' :

        gname = request.POST.get('gname')

        group = Group.objects.get(name=gname)
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.utxt)
        user.groups.add(group)
    

    return redirect('users_groups' , pk=pk)



def del_users_to_groups(request,pk,name):


    group = Group.objects.get(name=name)
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)
    user.groups.remove(group)
    
    

    return redirect('users_groups' , pk=pk)


