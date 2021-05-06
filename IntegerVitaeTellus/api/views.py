from rest_framework import generics, filters, viewsets
from django.contrib.auth.models import User

from recipes.models import Recipe
from .serializers import RecipeSerializer, UserSerializer

# class RecipeList(generics.ListCreateAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', 'author__username', 'ingredients', 'instructions']

# class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__username', 'ingredients', 'instructions']

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
