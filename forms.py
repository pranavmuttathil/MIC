from django import forms
from .models import Person
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(forms.Form):
    name = forms.CharField(label="username", max_length=24)
    email = forms.EmailField(label="email")
    password = forms.CharField(label="password", max_length=24)
    confirm_password = forms.CharField(label="Confirm Password", max_length=24)

class LoginForm(forms.Form):
    name = forms.CharField(label="username1", max_length=24)
    password = forms.CharField(label="password1",max_length=24)