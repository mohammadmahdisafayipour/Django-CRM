from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


def home(request):
    
    records = Record.objects.all()
    
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
    return render(request, 'home.html',context={'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out...")
    return redirect('/')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            obj = form.save()
            # authenticate and login
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username = username,password=password)
            login(request,user)
            messages.success(request,"You have Successfully Registered! Welcome")
            return redirect('/')
    else:
        form = SignUpForm()
        return render(request,'register.html',context={'form':form})
    return render(request,'register.html',context={'form':form})