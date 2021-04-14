from django.db import models
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    memberSince = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:profile", args=(self.user.username,))

class MyModel(models.Model):
    my_image = models.ImageField(upload_to='images/')
    