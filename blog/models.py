from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class BlogPost(models.Model):
    # get blog post for user query: blogpost_set() or BlogPost.objects.filter(user__id=id)
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)  # hello word -> hello-word
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f"/blog/{self.slug}/"

    def get_edit_url(self):
        return f"{self.get_absolute_url}/edit/"

    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"
