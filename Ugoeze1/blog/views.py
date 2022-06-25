from msilib.schema import ListView
from msilib.schema import CreateView
from msilib.schema import DetailView
from msilib.schema import UpdateView
from turtle import update
from django.shortcuts import render
from models import Post

# Create your views here.

class PostListView(ListView):
    model = Post


class POstCreateView(CreateView):
    model = Post

    fields = "__all__"

    success_url  = "reverse_lazy"("blog:all")


class PostDetialView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post

    fields = "__all__"

    success_url  = "reverse_lazy"("blog:all")

class PostDeleteView(UpdateView):
    model = Post

    fields = "__all__"

    success_url  = "reverse_lazy"("blog:all")





 
