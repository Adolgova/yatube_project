
# Create your views here.
from django.shortcuts import render

def index(request):
    templates = 'posts/index.html'
    return render(request, templates)

def group_posts(request, slug):
    templates = 'posts/index.html'
    return render(request, templates)

