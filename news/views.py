#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, PostCategory, Comment

class NewsList(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'news.html'
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


