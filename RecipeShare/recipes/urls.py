from django.urls import path
from . import views

urlpatterns = [
    path('main-ingredients', views.handle_main_ingredients, name='main-ingredients'),
    path('recipe-types/', views.handle_recipe_types, name='recipe-types'),
    path('cuisines/', views.handle_cuisines, name='cuisines'),

    path('', views.recipes, name='recipes'),
    path('<str:id>/', views.handle_recipe_pages, name='recipe-page'),
]
