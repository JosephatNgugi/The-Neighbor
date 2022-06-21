from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

# Create your views here.

def homepage(request):
    all_posts = Post.objects.all()
    all_hoods = NeighborHood.objects.all()
    posts = all_posts[::-1]
    hoods = all_hoods[::-1]
    
    context = {
        'posts':posts,
        'hoods':hoods,
        }
    return render(request, 'neighbor/home.html', context)

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

@login_required(login_url='/accounts/login/')
def profile(request,id):
    profile = UserProfile.objects.get(user = id)
    return render(request, 'user/profile.html', {"profile":profile})

@login_required(login_url='login')
def update_profile(request):
    user= request.user
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.id)
    else:
        user_form = UserUpdateForm(instance=request.user)
        prof_form = ProfileForm(instance=request.user.profile)
        
    context = {
        'user_form':user_form,
        'prof_form':prof_form,
        }
    return render(request, 'user/update-profile.html', context)

def create_hood(request):
    if request.method =="POST":
        form  = HoodForm(request.POST,request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('homepage')
    else:
        form = HoodForm()
    return render(request,'hood/newhood.html',{'form':form})

def hood(request,id):
    hood = NeighborHood.objects.get(id = id)
    biz = Business.objects.filter(neighbourhood=hood)
    all_posts = Post.objects.filter(hood=hood)
    posts = all_posts[::-1]
    if request.method == "POST":
        form = BusinessForm(request.POST)
        if form.is_valid():
            biz_form = form.save(commit=False)
            biz_form.neighbourhood = hood
            biz_form.user = request.user.profile
            biz_form.save()
            return redirect('hood', hood.id)
    else:
        form = BusinessForm()
    context ={
        'hood':hood,
        'business':biz,
        'posts':posts,
        'form':form,      
    }
    return render(request,'hood/hood.html',context)
