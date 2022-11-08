from enum import auto
from random import choices
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.forms import PasswordInput

Gender=(
    ('male','male'),
    ('female','female'),
    ('other','other')
)
class RegisterForm(UserCreationForm):
    name=forms.CharField(max_length=20)
    gender= forms.CharField(max_length=10 ,)
    dob= forms.DateField( widget=forms.DateInput())
    password=forms.CharField(widget=PasswordInput() , max_length=20)
    class Meta:
        model= User 
        fields= ['name','username','email','password','gender','dob']