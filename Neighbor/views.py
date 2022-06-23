from django.shortcuts import get_object_or_404, redirect, render
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
            return redirect('home')
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
            hood.user = request.user.profile
            hood.save()
            return redirect('home')
    else:
        form = HoodForm()
    return render(request,'hood/newhood.html',{'form':form})

def hood(request,id):
    hood = NeighborHood.objects.get(id = id)
    biz = Business.objects.filter(neighbourhood=hood)
    all_posts = Post.objects.filter(neighborhood=hood)
    members = UserProfile.objects.filter(neighborhood = hood )
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
        'members':members    
    }
    return render(request,'hood/hood.html',context)

def join_hood(request,id):
    neighborhood = get_object_or_404(NeighborHood,id=id)
    request.user.profile.neighborhood=neighborhood
    request.user.profile.save()
    return redirect('home')

def leave_hood(request,id):
    hood = get_object_or_404(NeighborHood,id=id)
    request.user.profile.neighborhood=None
    request.user.profile.save()
    return redirect('home')

def post(request,hood_id):
    hood = NeighborHood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('hood', hood.id)
    else:
        form = PostForm
    return redirect(request, 'neighbor/post.html', {'form':form})

def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Business.objects.filter(business_name__icontains=name).all()
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'neighbor/results.html', params)
    else:
        message = "You haven't searched for any Businesses"
    return render(request, "neighbor/results.html")
