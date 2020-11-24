from django.shortcuts import render, reverse
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from .models import User
from .forms import LoginForm, RegisterForm

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
    login_form = LoginForm()

    data = {
        'greeting': message,
        'form': login_form
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

def login(request):
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

    method = request.method
    # can be called while diplaying the login form
    # GET
    if method == 'GET':
        login_form = LoginForm()
    else:
        # can be called while submitting the form
        # POST
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_data = login_form.cleaned_data
            
            users = User.objects.filter(**login_data)
            if users:
                # get a new session from this request
                user = users[0]
                session = request.session
                session['username'] = login_data['username']
                session['profile_pic_url'] = user.profile_pic.url

                return HttpResponseRedirect(reverse('libapp:landing'))

    data['form'] = login_form
    return render(request, 'libmgmt/public/home.html', data)

class RegisterView(FormView):
    template_name = 'libmgmt/public/register.html'
    form_class = RegisterForm
    # It will render register.html with the RegisterForm instance passed as `form` attribute in the data

    def form_valid(self, form):
        ''' register_data = form.cleaned_data
        user = User(**register_data)
        user.save() '''

        form.save()

        return HttpResponseRedirect(reverse('libapp:home'))