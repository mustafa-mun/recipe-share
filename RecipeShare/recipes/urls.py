from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('<str:id>/', views.handle_recipe_pages, name='recipe-page')
]
