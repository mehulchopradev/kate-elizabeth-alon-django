from django.urls import path
from .views import show_home, show_register, register

# lib/

app_name = 'libapp'

urlpatterns = [
    path('home/', show_home, name='home'),
    path('sign-up/', show_register, name='signup'),
    path('register/', register, name='register')
]
