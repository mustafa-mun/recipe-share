from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from verify_email.email_handler import send_verification_email

# Create your views here.


def home_page(request):
    context = {  } # add contenxt later
    return render(request, 'base/home.html', context)

def sign_up(request):
    form = SignupForm().as_p
    context = { 'form': form }

    if request.method == 'POST':
        # handle POST request
        form = SignupForm(request.POST)
        if form.is_valid():
            crd = form.cleaned_data 
            try:
                user = User.objects.create_user(crd['username'], None, crd['password'])
            except Exception as e:
                messages.warning(request, e)
            # user is created and saved to the database at this point.
            return redirect('log-in')
        else:
            messages.warning(request, 'Form is not valid')
        

    return render(request, 'form.html', context)

def log_in(request):
    form = LoginForm().as_p
    context = { 'form': form}
        
    
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        
        user = authenticate(request, username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request, user)
            return redirect('home')
        else:
            # No backend authenticated the credentials
            messages.warning(request, 'Username or password is wrong')
        

    return render(request, 'form.html', context)

def log_out(request):
    # log out user if user is logged in
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('home')
        

