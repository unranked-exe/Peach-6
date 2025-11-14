from django.test import TestCase
from django.urls import reverse

class RecipesViewTest(TestCase):
    """Test suite for the recipes views."""

    fixtures = [
        'recipes/tests/fixtures/default_user.json',
        'recipes/tests/fixtures/valid_recipe.json'
    ]

    def setUp(self):
        self.url_list_recipes = reverse('list_recipes')
        self.url_get_recipe_valid = reverse('get_recipe', args=[1])

    def test_recipes_url(self):
        self.assertEqual(self.url_list_recipes, '/recipes/')

    def test_list_recipes_view(self):
        response = self.client.get(self.url_list_recipes)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes.html')
        self.assertIn('recipes', response.context)
        self.assertEqual(len(response.context['recipes']), 1)

    def test_get_recipe_view_valid_id(self):
        response = self.client.get(self.url_get_recipe_valid)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe.html')
        self.assertIn('recipe', response.context)
        self.assertEqual(response.context['recipe'].id, 1)

    def test_get_recipe_view_invalid_id(self):
        response = self.client.get(reverse('get_recipe', args=[999]))
        self.assertEqual(response.status_code, 404)