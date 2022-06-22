from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/sign-up/', views.UserRegistration, name='signup'),
    path('accounts/profile/<id>/',views.profile,name = 'profile'),
    path('accounts/profile/', RedirectView.as_view(url='/')),
    path('accounts/update/profile/',views.update_profile,name = 'updateProfile'), 
    path('create/new-hood/', views.create_hood, name='createHood'),
    path('hood/<id>/', views.hood, name='hood'),
    path('hood/join-hood/<id>/', views.join_hood, name='join-hood'),
    path('hood/leave/<id>/', views.leave_hood, name='leave-hood'),
    path('search/', views.search_business, name='search'),
    path('create/post/<hood_id>/', views.post, name='post')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)