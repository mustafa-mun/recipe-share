from django.contrib import admin
from .models import Recipe, MainIngredient, RecipeMainIngredient, Ingredient, RecipeIngredient
# Register your models here.


admin.site.register(Recipe)
admin.site.register(MainIngredient)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeMainIngredient)
admin.site.register(Ingredient)
