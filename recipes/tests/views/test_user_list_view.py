"""Tests of the user list view"""
from django.test import TestCase
from django.urls import reverse
from recipes.models import User
from recipes.tests.helpers import reverse_with_next

class UserListViewTestCase(TestCase):

    fixtures = ['recipes/tests/fixtures/default_user.json', 'recipes/tests/fixtures/other_users.json']

    def setUp(self):
        self.user = User.objects.get(username = '@johndoe')
        self.url = reverse('user_list')

    def test_user_list_url(self):
        self.assertEqual(self.url, '/users/')

    def test_get_user_list_redirects_when_not_logged_in(self):
        redirect_url = reverse_with_next('log_in', self.url)
        response = self.client.get(self.url)
        self.assertRedirects(response, redirect_url, status_code=302, target_status_code=200)

    def test_get_user_list_succesful(self):
        self.client.login(username = self.user.username, password = 'Password123')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_list.html')

    def test_user_list_content_and_sorting(self):
        self.client.login(username = self.user.username, password = "Password123")
        response = self.client.get(self.url)

        users_list = list(response.context['users'])
        self.assertEqual(len(users_list), 3)

        self.assertNotIn(self.user, users_list)

        self.assertEqual(users_list[0], User.objects.get(username = '@janedoe'))
        self.assertEqual(users_list[1], User.objects.get(username = '@peterpickles'))
        self.assertEqual(users_list[2], User.objects.get(username = '@petrapickles'))

        self.assertContains(response, "Jane Doe")
        self.assertContains(response, "Peter Pickles")
        self.assertContains(response, "Petra Pickles")

        self.assertNotContains(response, "John Doe")
