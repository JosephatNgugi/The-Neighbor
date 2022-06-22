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
        model = UserProfile
        fields = ['user', 'bio', 'avatar', 'neighborhood']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email'] 

class HoodForm(forms.ModelForm):
    class Meta:
        model = NeighborHood
        exclude = ('user',)     

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user','neighborhood')

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude =('posted_by','neighborhood')
