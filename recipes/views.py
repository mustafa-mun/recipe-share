from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q 
from .models import MainIngredient, Cuisine, PrepTime, Type, Recipe

def recipes(request):
     # check if user is authenticated
    if not request.user.is_authenticated:
        # user is not logged in
        return redirect('log-in') # redirect to login page
        
    main_ingredients = MainIngredient.objects.all()
    recipe_types = Type.objects.all()
    prep_times = PrepTime.objects.all()
    cuisines = Cuisine.objects.all()

    context = {
        'main_ingredients': main_ingredients,
        'recipe_types': recipe_types,
        'prep_times': prep_times,
        'cuisines': cuisines
    }
    if request.method == 'POST':
        form = request.POST
        # create recipe
        try:
            recipe = Recipe (
            recipe_author= request.user, 
            recipe_name = form['recipe_name'],
            recipe_method = form['recipe_method'],
            recipe_ingredients = form['recipe_ingredients'],
            recipe_cuisine = Cuisine.objects.get(cuisine_name = form['cuisine']),
            recipe_main_ingredient = MainIngredient.objects.get(ingredient_name = form['main_ingredient']),
            recipe_type = Type.objects.get(type_name = form['recipe_type']),
            recipe_prep_time = PrepTime.objects.get(prep_time = form['prep_time']),
            )

            # include optional fields if they exist
            if form['recipe_description'] != '':
                recipe.recipe_description = form['recipe_description']
            if form['recipe_image'] != '':
                recipe.recipe_image = form['recipe_image']
            recipe.save()

            return redirect('home')
        # handle errors
        except Exception as e:
            messages.warning(request, e)

    return render(request, 'recipes/create_recipe.html', context)

def advanced_search(request):
    main_ingredients = MainIngredient.objects.all()
    recipe_types = Type.objects.all()
    prep_times = PrepTime.objects.all()
    cuisines = Cuisine.objects.all()

    if request.method == 'POST':
        form = request.POST
        recipes = Recipe.objects.filter(
            Q(recipe_name__icontains=form['recipe_name']) &
            Q(recipe_description__icontains=form['recipe_description']) &
            Q(recipe_main_ingredient__ingredient_name__icontains=form['main_ingredient']) &
            Q(recipe_cuisine__cuisine_name__icontains=form['cuisine']) &
            Q(recipe_type__type_name__icontains=form['recipe_type']) & 
            Q(recipe_prep_time__prep_time__icontains=form['prep_time'])  
        ) 
        context = {
            'recipes': recipes,
            'msg': 'Found ' + str(len(recipes)) + ' results for your search query' 
        }
        return render(request, 'base/home.html', context)   
        
    context = {
        'main_ingredients': main_ingredients,
        'recipe_types': recipe_types,
        'prep_times': prep_times,
        'cuisines': cuisines
    }
    return render(request, 'recipes/search.html', context)

def handle_recipe_pages(request, id):
    recipe = Recipe.objects.get(id=id)
    
    context = {
        'recipe': recipe,
        
    }
    return render(request, 'recipes/recipe.html', context)

def get_main_ingredients(request):
    main_ingredients = MainIngredient.objects.all()
    context = { 
        'objects': main_ingredients,
        'obj_type': 'main-ingredients'
    }
    return render(request, 'obj.html', context)

def get_recipe_types(request):
    recipe_types = Type.objects.all()
    context = { 
        'objects': recipe_types,
        'obj_type': 'recipe_types'
    }
    return render(request, 'obj.html', context)

def get_cuisines(request):
    cuisines = Cuisine.objects.all()
    context = { 
        'objects': cuisines,
        'obj_type': 'cuisines'
    }
    return render(request, 'obj.html', context)

def handle_main_ingredients(request, id):
    recipes = Recipe.objects.filter(recipe_main_ingredient=id)
    context = {
        'recipes': recipes,
    } 
    return render(request, 'base/home.html', context)

def handle_recipe_types(request, id):
    recipes = Recipe.objects.filter(recipe_type=id)
    context = {
        'recipes': recipes,
    } 
    return render(request, 'base/home.html', context)

def handle_cuisines(request, id):
    recipes = Recipe.objects.filter(recipe_cuisine=id)
    context = {
        'recipes': recipes,
    } 
    return render(request, 'base/home.html', context)

def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    main_ingredients = MainIngredient.objects.all()
    recipe_types = Type.objects.all()
    prep_times = PrepTime.objects.all()
    cuisines = Cuisine.objects.all()

    context = {
        'main_ingredients': main_ingredients,
        'recipe_types': recipe_types,
        'prep_times': prep_times,
        'cuisines': cuisines,
        'recipe': recipe
    }

    if request.method == 'POST':
        try:
            form = request.POST
            recipe.recipe_name = form['recipe_name']
            recipe.recipe_method = form['recipe_method']
            recipe.recipe_ingredients = form['recipe_ingredients']
            recipe.recipe_main_ingredient =  MainIngredient.objects.get(ingredient_name = form['main_ingredient'])
            recipe.recipe_cuisine = Cuisine.objects.get(cuisine_name = form['cuisine'])
            recipe.recipe_type = Type.objects.get(type_name = form['recipe_type'])
            recipe.recipe_prep_time = PrepTime.objects.get(prep_time = form['prep_time'])

            # include optional fields if they exist
            if form['recipe_description'] != '':
                recipe.recipe_description = form['recipe_description']
            if form['recipe_image'] != '':
                recipe.recipe_image = form['recipe_image']
            # save the recipe    
            recipe.save()

            return redirect('home')
        # handle errors
        except Exception as e:
            messages.warning(request, e)

    return render(request, 'recipes/update_recipe.html', context)

def delete_recipe(request, id):
    recipe = Recipe.objects.get(id = id);
    if request.user is recipe.recipe_author or request.user.is_superuser:

        if request.method == 'GET':
            context = { 'obj': recipe.recipe_name }
            return render(request, 'delete.html', context)

        if request.method == 'POST':
            recipe.delete()
            return redirect('home')  # Redirect to a home page
    else:
        context = {'error': 'You are not the owner of this recipe'}
        return render(request, 'error.html', context)