from django import forms
from .models import Wear
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class WearForm(forms.ModelForm):
    class Meta:
        model = Wear
        fields = ['name', 'size', 'color', 'price', 'category_id']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


