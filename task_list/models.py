from django.db import models

# Create your models here.


class TaskList(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    finished = models.BooleanField(default=False)

