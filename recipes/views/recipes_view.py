from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from recipes.models.recipe import Recipe

def list_recipes(request):
    """
    Display all recipes page.

    This view renders the page of all recipes. It does not require
    authentication, allowing both logged-in and anonymous users to
    access all recipes.
    """
    context = {'recipes': Recipe.objects.all()}
    return render(request, 'recipes.html', context)


def get_recipe(request, recipe_id):
    """
    Display a single recipe page.

    This view renders the page for a specific recipe identified by
    its ID. It does not require authentication, allowing both logged-in
    and anonymous users to access the recipe details.
    """
    try:
        context = {'recipe': Recipe.objects.get(id=recipe_id)}
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    else:
        return render(request, 'recipe.html', context)