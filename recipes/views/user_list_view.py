from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from recipes.models import User

class UserListView(LoginRequiredMixin, ListView):
    """
    Displays a list of all users, excluding the currently logged-in user.
    """
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(pk = self.request.user.pk)