from django.shortcuts import render, reverse
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from .models import User

# Create your views here.
def show_home(request):
    dtobj = datetime.now()
    hour = dtobj.hour
    if hour >= 0 and hour < 12:
        message = 'Good morning'
    elif hour >= 12 and hour < 16:
        message = 'Good afternoon'
    else:
        message = 'Good evening'

    data = {
        'greeting': message
    }

    return render(request, 'libmgmt/public/home.html', data)

def show_register(request):
    return render(request, 'libmgmt/public/register.html')

def register(request):
    # request -> collect data from the client
    data = request.POST
    username = data['username']
    password = data['password']
    country = data['country']
    gender = data['gender']
    # print(username, password, country, gender)

    user = User(username=username, password=int(password), country=country, gender=gender)
    user.save()

    return HttpResponseRedirect(reverse('libapp:home'))

def authenticate(request):
    data = request.POST
    username, password = data['username'], data['password']

    users = User.objects.filter(username=username, password=password)
    if users:
        # get a new session from this request
        session = request.session
        session['username'] = username

        return HttpResponseRedirect(reverse('libapp:landing'))
    return HttpResponseRedirect(reverse('libapp:home'))
