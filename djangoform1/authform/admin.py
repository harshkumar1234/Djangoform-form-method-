from django.contrib import admin
from .models import Register

@admin.register(Register)
# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display= ['name','username','password','email','gender','dateofbirth']

