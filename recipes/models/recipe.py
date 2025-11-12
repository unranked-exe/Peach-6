from django.db import models
from .user import User

class Recipe(models.Model):

    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    ingredients = models.TextField()
    instructions = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    difficulty_level = models.CharField(max_length=50)
    preparation_time_mins = models.IntegerField(help_text="Preparation time in minutes")

#Sample init recipe1 = Recipe(name = "Lasagna", author=user1,ingredients = "Ingredients", instructions = "Sample Instructions", difficulty_level = "Easy", preparation_time_mins = 30)
#user1 = User.objects.first
    def __str__(self):
        return f"{self.name} by {self.author.username}"