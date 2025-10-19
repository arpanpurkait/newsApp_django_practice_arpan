

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
                    LoginRequiredMixin,
                    UserPassesTestMixin # new
                )

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    fields = ["title", "content"]
    template_name = "article_edit.html"
    
class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

class ArticleCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView): # new
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        "author",
    )
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)