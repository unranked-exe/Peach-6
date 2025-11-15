from django.db import models

class FoodTag(models.Model):
    tag_name = models.CharField(max_length=50, blank=True, unique=True)

    # Use this to create the tags!
    # From CLI:
    # from recipes.models.foodtag import FoodTag

    # FoodTag.objects.create(tag_name="Halal")
    # FoodTag.objects.create(tag_name="Kosher")
    # FoodTag.objects.create(tag_name="Vegan")
    # FoodTag.objects.create(tag_name="Gluten-free")
    # etc
    # I used ManyToMany relationship so we can make a checklist of tags in the form
    # E.g. when making form use CheckboxSelectMultiple widget so user can choose any tags

    def __str__(self):
        return self.tag_name