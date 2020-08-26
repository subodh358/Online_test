from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from .models import CustomUser
 
 
class SignUpForm(UserCreationForm):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20)
    prn = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null= False, blank= False)
 
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ( 'prn','first_name', 'last_name', 'email')