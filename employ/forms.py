from django import forms
from .models import employ
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmployForm(forms.ModelForm):
    class Meta:
        model = employ
        fields = ['name', 'email', 'age', 'course']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']