"""firstproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import hello, contactus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('home/', TemplateView.as_view(template_name="home.html"), name='home'),
    path('about-us/', TemplateView.as_view(template_name="aboutus.html"), name='about'),
    path('contact-us/', contactus, name='contact'),
    path('lib/', include('libmgmt.urls')) # include the non root app urls and mount it in the root app urls
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
