from recipes.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

class UserProfileView(LoginRequiredMixin, DetailView):
    """
    Displays the profile page for a single User object.
    Requires login and retrieves the target user based on PK from the URL.
    """
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user'