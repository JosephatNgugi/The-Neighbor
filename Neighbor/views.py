from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from .models import *

# Create your views here.

def homepage(request):
    all_posts = Post.objects.all()
    posts = all_posts[::-1]
    return render(request, 'neighbor/home.html',{'posts':posts})

def UserRegistration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            InputPassword = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=InputPassword)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})
