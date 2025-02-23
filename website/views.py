from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm,AddRecord
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





def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'record':customer_record})
    else:
        messages.success(request,"You Must Be Logged In To View That Page...")
        return redirect('/')


def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Records Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request,"You Must Be Logged in to delete a record...")
        
 
def add_record(request):
    if request.user.is_authenticated:
        form = AddRecord(request.POST or None)
        context = {"form":form}
        if form.is_valid():
            obj_form = form.save()
            messages.success(request,"Record Added...")
            return redirect('home')
            # context['form'] = AddRecord()
        return render(request,'add_record.html',context=context)
    else:
        messages.success(request,"You are not Logged In...")
        return redirect('home')
    

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecord(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Has Been Updated")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})

    else:
        messages.success(request,"You Must Be Logged In...")
        return redirect('home')