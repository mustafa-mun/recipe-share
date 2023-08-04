from django.contrib import admin
from .models import Recipe, MainIngredient, PrepTime, Cuisine,  Type# Register your models here.


admin.site.register(Recipe)
admin.site.register(MainIngredient)
admin.site.register(PrepTime)
admin.site.register(Cuisine)
admin.site.register(Type)