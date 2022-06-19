from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile, User
        fields = ['username', 'email', 'user', 'bio', 'avatar', 'neighborhood']
        