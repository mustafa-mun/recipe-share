from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    context = {  } # add contenxt later
    return render(request, 'base/home.html', context)

def sign_up(request):
    form = UserForm().as_p
    context = { 'form': form }
    
    if request.method == 'POST':
        # handle POST request
        crd = request.POST # credentials 
        try:
            user = User.objects.create_user(crd['username'], None, crd['password'])
        except:
            messages.warning(request, 'error while creating user')

        # user is created and saved to the database at this point.
        return redirect('home')


    return render(request, 'form.html', context)