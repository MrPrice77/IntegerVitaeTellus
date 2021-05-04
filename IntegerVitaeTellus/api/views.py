from rest_framework import generics, filters

from recipes import models
from .serializers import RecipeSerializer

class RecipeList(generics.ListCreateAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__username', 'ingredients', 'instructions']

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = RecipeSerializer
