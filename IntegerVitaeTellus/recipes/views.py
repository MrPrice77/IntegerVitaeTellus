from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipe_new.html'
    fields = ['title', 'my_image', 'ingredients', 'instructions', 'source']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    template_name = 'recipe_edit.html'
    fields = ['title', 'my_image', 'ingredients', 'instructions', 'source']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('recipes:home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author    