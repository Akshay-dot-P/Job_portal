from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=100)
    link = models.TextField()
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.name

