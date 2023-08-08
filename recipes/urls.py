from django.urls import path
from . import views

urlpatterns = [
    path('main-ingredients/', views.get_main_ingredients, name='main-ingredients'),
    path('recipe-types/', views.get_recipe_types, name='recipe-types'),
    path('cuisines/', views.get_cuisines, name='cuisines'),

    path('', views.recipes, name='recipes'),
    path('<str:id>/', views.handle_recipe_pages, name='recipe-page'),
    
    path('main-ingredients/<str:id>/', views.handle_main_ingredients, name='main-ingredients-id'),
    path('recipe-types/<str:id>/', views.handle_recipe_types, name='recipe-types-id'),
    path('cuisines/<str:id>/', views.handle_cuisines, name='cuisines-id'),

    path('advanced-search', views.advanced_search, name='advanced-search'),

    path('update-recipe/<str:id>', views.update_recipe, name='update-recipe'),
    path('delete-recipe/<str:id>', views.delete_recipe, name='delete-recipe')
]
