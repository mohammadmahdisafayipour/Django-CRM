from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def home(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You Have Been Loged In")

            return redirect('/')
        else:
            messages.success(request,"There Was An Error Logging")
    return render(request, 'home.html',context={})


def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out...")
    return redirect('/')


def register_user(request):
#     # if  12==12:
#     #     return redirect('/')

    return render(request,'register.html',context={})