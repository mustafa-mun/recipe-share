from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    context = { 'title': 'home' } # add contenxt later
    return render(request, 'base/home.html', context)