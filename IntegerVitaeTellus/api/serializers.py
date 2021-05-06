from rest_framework import serializers

from recipes.models import Recipe
from django.contrib.auth.models import User

# class RecipeSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'id',
#             'title',
#             'author',
#             'created',
#             'my_image',
#             'ingredients',
#             'instructions',
#             'source',
#         )
#         model = Recipe

class NestedRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'created', 'updated', 'body')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class RecipeSerializer(serializers.ModelSerializer):
    author_detail = NestedUserSerializer(read_only=True, source='author')
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'author_detail', 'created', 'my_image', 'ingredients', 'instructions', 'source')

class UserSerializer(serializers.ModelSerializer):
    recipe_detail = NestedRecipeSerializer(read_only=True, many=True, source='recipe_list')
    class Meta:
        model = User
        fields = ('id', 'username', 'recipe_detail')