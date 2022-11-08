from email import message
from django.contrib import messages
from operator import imod
from django.shortcuts import HttpResponse, render
from .forms import  RegisterForm
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login,logout, authenticate

# Create your views here.
def register(request):
    if request.method=='POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            # return ("account created successfully")
            messages.success(request ,"account created successfully")
            return render (request , 'authuser/login.html')
    else: 
        form= RegisterForm()

    return render(request , 'authform/register.html',{'form':form})
            
def Login(request):
    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']
        user= authenticate(request , username=username, password=password)
        if user is not None:
            form=login(request,user)
            messages.success(request,"welcome {username}")
            return render(request , 'authform1/home.html' )
    else:
        form= AuthenticationForm()
    return render(request , 'authform/login.html' , {'form':form})


            
