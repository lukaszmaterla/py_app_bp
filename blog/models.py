from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.TextField()
    slug = models.SlugField() # hello word -> hello-word
    content = models.TextField(null=True, blank=True)
