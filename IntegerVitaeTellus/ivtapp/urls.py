from django.urls import path

from . import views

app_name = 'ivtapp'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='home'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='detail'),
    path('recipe/new/', views.RecipeCreateView.as_view(), name='new'),
    path('recipe/<int:pk>/edit/', views.RecipeEditView.as_view(), name='edit'),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='delete')
]