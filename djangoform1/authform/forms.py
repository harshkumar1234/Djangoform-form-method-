from django import   forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
 
Gender=(
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other')
)
class RegisterForm(UserCreationForm):
    name= forms.CharField(max_length=20)
    username=forms.CharField(max_length=20)
    email= forms.EmailField(max_length=20)
    password= forms.CharField(widget=forms.PasswordInput , max_length=20)
    gender= forms.CharField(max_length=20)
    dateofbirth= forms.DateField()
    class Meta:
        model = User 
        fields= ['name','username','email','password','gender','dateofbirth']
        exclude=['password2']
           