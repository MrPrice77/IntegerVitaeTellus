from django.urls import path
from rest_framework.routers import DefaultRouter

# from .views import RecipeDetail, RecipeList
from .views import RecipeViewSet, UserViewSet

# urlpatterns = [
#     path('', RecipeList.as_view()),
#     path('<int:pk>/', RecipeDetail.as_view()),
# ]


router = DefaultRouter()
router.register('', RecipeViewSet, basename='recipes')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls
