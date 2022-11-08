from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password= models.CharField(max_length=10)
    email= models.EmailField(max_length=20)
    gender= models.CharField(max_length=20)
    dateofbirth= models.CharField(max_length=10)
    

