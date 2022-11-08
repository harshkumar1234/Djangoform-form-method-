from django.http import HttpResponseRedirect

from django.shortcuts import render
from .forms import SignUPForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
# this is signup function
def sign_up(request):
#  if  not request.user.is_login:
    if request.method =='POST':   
     fm=SignUPForm(request.POST)
     if fm.is_valid():
        messages.success(request,'Account creeated successfully !!')
        fm.save()
        return HttpResponseRedirect('/login/')
    else:
        fm=SignUPForm()
    return render(request,'myapp/signup.html',{'form':fm})
#  else:
#      return HttpResponseRedirect('/profile/')

#this is login function
def logIn(request):
 if request.user.is_authenticated:
    if request.method =='POST':   
     fm=AuthenticationForm(request=request,data=request.POST)
     if fm.is_valid():
         uname=fm.cleaned_data['username']
         upass=fm.cleaned_data['password']
         user=authenticate(username=uname,password=upass)
         if user is not None:
             login(request,user)
         return HttpResponseRedirect('/profile/')


    #     messages.success(request,'THANK YOU FOR LOGIN')
    #     fm.save()
    else:
        fm=AuthenticationForm()
    return render(request,'myapp/login.html',{'form':fm})
 else:
     return HttpResponseRedirect('/signup/')
# this is userprofile
def user_profile(request):
    if request.user.is_authenticated:   
     return render (request, 'myapp/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')



# this is logout function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
    
# user changed password
def user_change_pass(request):
 if request.user.is_authenticated:
    if request.method=='POST':
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            return HttpResponseRedirect('/profile/')
    else:
        fm=PasswordChangeForm(user=request.user)
        return render(request,'myapp/changepass.html',{'form':fm})
 else:
     return HttpResponseRedirect('/signup/')

