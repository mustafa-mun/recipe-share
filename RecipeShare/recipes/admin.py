from django.contrib import admin
from .models import Recipe, MainIngredient, RecipeMainIngredient, Ingredient, RecipeIngredient, PrepTime, Cuisine, RecipePrepTimes, RecipeCuisine, Type, RecipeTypes
# Register your models here.


admin.site.register(Recipe)
admin.site.register(MainIngredient)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeMainIngredient)
admin.site.register(Ingredient)
admin.site.register(PrepTime)
admin.site.register(RecipePrepTimes)
admin.site.register(Cuisine)
admin.site.register(RecipeCuisine)
admin.site.register(Type)
admin.site.register(RecipeTypes)