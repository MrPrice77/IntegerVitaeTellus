from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('recipe/list/', views.RecipeListView.as_view(), name='list'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='detail'),
    path('recipe/new/', views.RecipeCreateView.as_view(), name='new'),
    path('post/<int:pk>/edit/', views.RecipeEditView.as_view(), name='edit'),
    path('post/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='delete'),
]