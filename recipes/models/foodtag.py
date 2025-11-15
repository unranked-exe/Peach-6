from django.db import models

class Food_tag(models.Model):
    tag_name = models.charField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.name