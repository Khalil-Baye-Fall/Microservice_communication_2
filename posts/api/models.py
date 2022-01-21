from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)