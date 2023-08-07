from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from recipes.models import Recipe
# Create your views here.


def home_page(request):
    q = request.GET.get('q')
    if q is not None:
        recipes = Recipe.objects.filter(recipe_name__icontains=q)
    else:
        recipes = Recipe.objects.all()
    context = { 'recipes':recipes } # add contenxt later
    return render(request, 'base/home.html', context)

def sign_up(request):
    if request.method == 'POST':
        # handle POST request
        crd = request.POST
        if crd['password'] != crd['password2']:
            messages.warning(request, 'Passwords do not match')
            return render(request, 'base/signup.html')
        # try to sign the user up
        try:
            user = User.objects.create_user(crd['username'], None, crd['password'])
        except Exception as e:
            messages.warning(request, e)
        # user is created and saved to the database at this point.
        return redirect('log-in')

        

    return render(request, 'base/signup.html')

def log_in(request):
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
        

    return render(request, 'base/login.html')

def log_out(request):
    # log out user if user is logged in
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('home')

def user_profile(request, id):
    user = User.objects.get(id=id)
    recipes = Recipe.objects.filter(recipe_author=user)
    context = { 
        'recipes': recipes,
        'msg': 'Recipes posted by ' + user.username + ":"
    }
    return render(request, 'base/home.html', context)