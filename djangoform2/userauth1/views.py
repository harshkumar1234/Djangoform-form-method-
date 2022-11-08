from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method=='POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            messages.success("Registered successfully")
            form.save()
            return render('login/')
    else:
        form = RegisterForm()
    return render(request , 'userauth1/register.html', {'form':form})
