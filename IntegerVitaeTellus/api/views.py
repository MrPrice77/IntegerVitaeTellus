from rest_framework import generics

from recipes import models
from .serializers import RecipeSerializer

class RecipeList(generics.ListCreateAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = RecipeSerializer
