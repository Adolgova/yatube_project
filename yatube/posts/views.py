
# Create your views here.
from cgitb import text
from turtle import title
from typing import Text
from django.shortcuts import render

def index(request):
    templates = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, templates, context)

def group_posts(request, slug):
    templates = 'posts/group_list.html'
    text  = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, templates, context)