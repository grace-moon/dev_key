from django.db import models
from . import tuple

class Post(models.Model):
    program = models.CharField(max_length=200)
    cmd_category = models.CharField(choices=tuple.category_item, max_length=200)
    cmd_name = models.CharField(max_length=200)
    cmd_description = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

