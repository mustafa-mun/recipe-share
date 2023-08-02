from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Recipe(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  recipe_author = models.ForeignKey(
      User,
      on_delete=models.SET_NULL,
      null=True
  )
  recipe_name = models.CharField(max_length=150, unique=True)
  recipe_description = models.TextField(null=True, blank=True)
  recipe_method = models.TextField(default="")
  recipe_ingredients = models.TextField(default="", max_length=2000)
  recipe_image = models.TextField(default="https://thehalalworld.com/uploads/pages/Sardine-tea-sandwiches.jpg")
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
    
  def __str__(self) -> str:
    return self.recipe_name


class Cuisine(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  cuisine_name = models.CharField(max_length=100, unique=True)
    
  def __str__(self) -> str:
    return self.cuisine_name
  
class RecipeCuisine(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  recipe = models.ForeignKey(
      Recipe,
      on_delete=models.CASCADE,
      null=True
  )  
  cuisine = models.ForeignKey(
      Cuisine,
      on_delete=models.CASCADE,
      null=True
  )
  
  def __str__(self) -> str:
    return str(self.id)
  

class Type(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  type_name = models.CharField(max_length=100, unique=True)
    
  def __str__(self) -> str:
    return self.type_name
  
class RecipeTypes(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  recipe = models.ForeignKey(
      Recipe,
      on_delete=models.CASCADE,
      null=True
  )  
  type = models.ForeignKey(
      Type,
      on_delete=models.CASCADE,
      null=True
  )
  
  def __str__(self) -> str:
    return str(self.id)

class MainIngredient(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  ingredient_name = models.CharField(max_length=100, unique=True)
    
  def __str__(self) -> str:
    return self.ingredient_name
  
class RecipeMainIngredient(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  recipe = models.ForeignKey(
      Recipe,
      on_delete=models.CASCADE,
      null=True
  )  
  main_ingredient = models.ForeignKey(
      MainIngredient,
      on_delete=models.CASCADE,
      null=True
  )
  
  def __str__(self) -> str:
    return str(self.id)

class PrepTime(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  prep_time = models.CharField(max_length=50, unique=True)
    
  def __str__(self) -> str:
    return self.prep_time
  
class RecipePrepTimes(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  recipe = models.ForeignKey(
      Recipe,
      on_delete=models.CASCADE,
      null=True
  )  
  prep_time = models.ForeignKey(
      PrepTime,
      on_delete=models.CASCADE,
      null=True
  )
  
  def __str__(self) -> str:
    return str(self.id)