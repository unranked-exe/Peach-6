from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .user import User
from .foodtag import Food_tag

class Recipe(models.Model):

    name = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', blank=False)
    ingredients = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    difficulty_level = models.CharField(max_length=50, blank=False)
    preparation_time_mins = models.IntegerField(help_text="Preparation time in minutes", blank=False, validators=[MinValueValidator(1), MaxValueValidator(1440)])
    tags = models.ManyToManyField(Food_tag, blank=True)

#Sample init 
# user1 = User.objects.first()
# recipe1 = Recipe(name = "Lasagna", author=user1, ingredients = "Ingredients", instructions = "Sample Instructions", difficulty_level = "Easy", preparation_time_mins = 30)

    def __str__(self):
        return f"{self.name} by {self.author.username}"