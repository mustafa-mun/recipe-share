from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MainIngredient, Cuisine, PrepTime, Type, Recipe
from .forms import MainIngredientForm

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
            recipe = Recipe(
            recipe_author=request.user, 
            recipe_name = form['recipe_name'],
            recipe_method = form['recipe_method'],
            recipe_ingredients = form['recipe_ingredients'],
            recipe_cuisine = form['cuisine'],
            recipe_main_ingredient = form['main_ingredient'],
            recipe_type = form['recipe_type'],
            recipe_prep_time = form['prep_time']
            )
            # include optional fields if they exist
            if form['recipe_description'] is not '':
                recipe.recipe_description = form['recipe_description']
            if form['recipe_image'] is not '':
                recipe.recipe_image = form['recipe_image']
            recipe.save()
         
            return redirect('home')
        # handle errors
        except Exception as e:
            messages.warning(request, e)

    return render(request, 'recipes/create_recipe.html', context)


def handle_recipe_pages(request, id):
    recipe = Recipe.objects.get(id=id)

    context = {
        'recipe': recipe,
        
    }
    return render(request, 'recipes/recipe.html', context)

def create_main_ingredients(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            form = MainIngredientForm().as_p
            context = { 'form': form }
            return render(request, 'form.html', context)
        
        if request.method == 'POST':
            form = MainIngredientForm(request.POST)
            if form.is_valid():
                form.save()
    return redirect('home')  # Redirect to a home page