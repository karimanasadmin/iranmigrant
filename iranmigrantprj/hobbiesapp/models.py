from django.db import models

class Hobby(models.Model):
    hobby_name = models.CharField(max_length=100)
    description = models.TextField()
    # additional detail fields
    difficulty_level = models.CharField(max_length=100)
    # ...

    def __str__(self):
        return self.hobby_name
