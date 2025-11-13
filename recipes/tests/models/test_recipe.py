from django.test import TestCase
from django.core.exceptions import ValidationError

import datetime

from recipes.models import Recipe

class RecipeTestCase(TestCase):
    
    fixtures = [
        'recipes/tests/fixtures/default_user.json',
        'recipes/tests/fixtures/valid_recipe.json'
    ]

    def setUp(self):
        self.recipe = Recipe.objects.get(pk=1)
    
    def test_valid_recipe(self):
        self._assert_recipe_is_valid()


    # Name field tests
    def test_name_cannot_be_blank(self):
        self.recipe.name = ''
        self._assert_recipe_is_invalid()
    
    def test_name_can_be_100_characters_long(self):
        self.recipe.name = 'd' * 100
        self._assert_recipe_is_valid()
    
    def test_name_cannot_be_over_100_characters_long(self):
        self.recipe.name = 'd' * 101
        self._assert_recipe_is_invalid()

    # Author field tests
    def test_author_cannot_be_null(self):
        self.recipe.author = None
        self._assert_recipe_is_invalid()
    
    # Ingredients field tests
    def test_ingredients_cannot_be_blank(self):
        self.recipe.ingredients = ''
        self._assert_recipe_is_invalid()
    
    # Instructions field tests
    def test_instructions_cannot_be_blank(self):
        self.recipe.instructions = ''
        self._assert_recipe_is_invalid()
    
    # Difficulty level field tests
    def test_difficulty_level_cannot_be_blank(self):
        self.recipe.difficulty_level = ''
        self._assert_recipe_is_invalid()
    
    def test_difficulty_level_can_be_50_characters_long(self):
        self.recipe.difficulty_level = 'e' * 50
        self._assert_recipe_is_valid()
    
    def test_difficulty_level_cannot_be_over_50_characters_long(self):
        self.recipe.difficulty_level = 'e' * 51
        self._assert_recipe_is_invalid()
    
    # Preparation time field tests
    def test_preparation_time_mins_cannot_be_null(self):
        self.recipe.preparation_time_mins = None
        self._assert_recipe_is_invalid()
    
    def test_preparation_time_mins_cannot_be_negative(self):
        self.recipe.preparation_time_mins = -10
        self._assert_recipe_is_invalid()

    def test_preparation_time_mins_cannot_be_zero(self):
        self.recipe.preparation_time_mins = 0
        self._assert_recipe_is_invalid()
    
    def test_preparation_time_mins_can_be_one(self):
        self.recipe.preparation_time_mins = 1
        self._assert_recipe_is_valid()
    
    def test_preparation_time_mins_can_be_maximum_value(self):
        self.recipe.preparation_time_mins = 1440
        self._assert_recipe_is_valid()
    
    def test_preparation_time_mins_cannot_exceed_maximum_value(self):
        self.recipe.preparation_time_mins = 1441
        self._assert_recipe_is_invalid()

    def _assert_recipe_is_valid(self):
        try:
            self.recipe.full_clean()
        except ValidationError:
            self.fail("Test recipe should be valid")

    def _assert_recipe_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()