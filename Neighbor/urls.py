from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/sign-up/', views.UserRegistration, name='signup'),
    re_path(r'^accounts/profile/(?P<id>\d+)/',views.profile,name = 'profile'),
    path('accounts/profile/', RedirectView.as_view(url='/')),
    path('accounts/update/profile/',views.update_profile,name = 'updateProfile'), 
    path('create/new-hood/', views.create_hood, name='createHood'),
    re_path(r'^hood/(?P<id>\d+)/', views.hood, name='hood'),
    re_path(r'^hood/join-hood/(?P<id>\d+)/', views.join_hood, name='join-hood'),
    re_path(r'^hood/leave/(?P<id>\d+)/', views.leave_hood, name='leave-hood'),
    path('search/', views.search_business, name='search'),
    re_path(r'^create/post/(?P<hood_id>\d+)/', views.post, name='post')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)