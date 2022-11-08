from dataclasses import fields
from django.contrib.auth.models import User
from django.forms.fields import ChoiceField, Field
from django.contrib.auth.forms import UserCreationForm

class SignUPForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
