from django.db import models
from django.urls import reverse

class Recipe(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    my_image = models.ImageField(upload_to='images/', null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=200, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('recipes:detail', args=(self.id,))

    class Meta:
        ordering = ['-created']