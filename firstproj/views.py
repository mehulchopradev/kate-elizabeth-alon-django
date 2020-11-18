from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('Hello World')

def home(request):
    # return HttpResponse('<html><body><h2>Welcome to my app</h2></body></html>')
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    # Imagine that the contact email and phone is coming from the database
    email = 'mehulc@hey.com'
    mobile = '99878688767'

    data = {
        'email': email,
        'mobile': mobile
    }

    return render(request, 'contactus.html', data)