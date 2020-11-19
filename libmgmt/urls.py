from django.urls import path
from .views import show_home, show_register, register, authenticate
from .private_views import show_landing

# lib/

app_name = 'libapp'

urlpatterns = [
    path('home/', show_home, name='home'),
    path('sign-up/', show_register, name='signup'),
    path('register/', register, name='register'),
    path('auth/', authenticate, name='auth'),
    path('private/landing/', show_landing, name='landing')
]
