from django.shortcuts import render

from .models import *

# Create your views here.

def homepage(request):
    all_posts = Post.objects.all()
    posts = all_posts[::-1]
    return render(request, 'neighbor/home.html',{'posts':posts})