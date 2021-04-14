from django.db import models
from django.urls import reverse

class Recipes(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True)
    ingredients = models.CharField(max_length=500, null=True, blank=True)
    instructions = models.CharField(max_length=1000, null=True, blank=True)
    source = models.CharField(max_length=200, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("recipe:detail", args=(self.id,))

    class Meta:
        ordering = ['-created']