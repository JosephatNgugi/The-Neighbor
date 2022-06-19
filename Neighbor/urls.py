from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/sign-up/', views.UserRegistration, name='signup'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)