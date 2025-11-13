from django.shortcuts import render
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