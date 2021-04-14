from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Recipes

class RecipeListView(ListView):
    model = Recipes
    template_name = 'home.html'

class RecipeDetailView(DetailView):
    model = Recipes
    template_name = 'recipe_detail.html'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipes
    template_name = 'recipe_new.html'
    fields = ['body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipes
    template_name = 'recipe_edit.html'
    fields = ['body']

    def test_funct(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Recipes
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('index.html')

    def test_func(self):
        recipe = self.get_object()
        return super.request.user == recipe.author