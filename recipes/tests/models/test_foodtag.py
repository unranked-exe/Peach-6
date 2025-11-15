from django.test import TestCase
from django.core.exceptions import ValidationError

from recipes.models import FoodTag

class FoodTagTestCase(TestCase):

    """Unit tests for the FoodTag model."""

    fixtures = [
        'recipes/tests/fixtures/valid_foodtag.json'
    ]

    def setUp(self):
        self.foodtag = FoodTag.objects.get(pk=1)

    def test_valid_foodtag(self):
        self._assert_foodtag_is_valid()

    def test_max_tag_name_length_cannot_be_more_than_50_chars(self):
        self.foodtag.tag_name = 'q' * 51
        self._assert_tag_name_is_invalid()

    def test_max_tag_name_length_can_be_50_chars(self):
        self.foodtag.tag_name = 'q' * 50
        self._assert_tag_name_is_valid()
    
    def test_foodtag_tag_name_can_be_blank(self):
        self.foodtag.tag_name = ''
        self._assert_recipe_is_valid()

    def _assert_foodtag_is_valid(self):
        try:
            self.foodtag.full_clean()
        except ValidationError:
            self.fail("Test foodtag should be valid")

    def _assert_foodtag_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.foodtag.full_clean()
    