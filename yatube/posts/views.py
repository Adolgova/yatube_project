
# Create your views here.
from cgitb import text
from turtle import title
from typing import Text
from django.shortcuts import render
from .models import Post, Group

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    templates = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'posts': title,
    }
    return render(request, templates, context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)