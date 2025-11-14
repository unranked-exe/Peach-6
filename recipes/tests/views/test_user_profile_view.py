"""Tests of the user profile view"""
from django.test import TestCase
from django.urls import reverse
from recipes.models import User
from recipes.tests.helpers import reverse_with_next

class UserProfileViewTestCase(TestCase):

    fixtures = ['recipes/tests/fixtures/default_user.json', 'recipes/tests/fixtures/other_users.json']

    def setUp(self):
        self.useer_client = User.objects.get(username = '@johndoe')

        self.user_to_view = User.objects.get(pk = 2)

        self.url = reverse('user_profile', kwargs={'pk': self.user_to_view.pk})

    def test_user_profile_url(self):
        self.assertEqual(self.url, f'/users/{self.user_to_view.pk}/')

    def test_user_profile_succesful(self):

        self.client.login(username = self.useer_client.username, password = 'Password123')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')

        self.assertEqual(response.context['user'], self.user_to_view)

        self.assertContains(response, self.user_to_view.username)
        self.assertContains(response, self.user_to_view.first_name)
        self.assertContains(response, self.user_to_view.last_name)
        self.assertContains(response, self.user_to_view.full_name())
        self.assertContains(response, self.user_to_view.gravatar())

    def test_get_user_profile_redirects_when_not_logged_in(self):
        redirect_url = reverse_with_next('log_in', self.url)
        response = self.client.get(self.url)
        self.assertRedirects(response, redirect_url, status_code=302, target_status_code=200)

    def test_user_profile_with_invalid_pk(self):
        self.client.login(username = self.useer_client.username, password = 'Password123')
        bad_url = reverse('user_profile', kwargs={'pk':300})
        response = self.client.get(bad_url)
        self.assertEqual(response.status_code, 404)
