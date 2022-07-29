
# Create your views here.
from django.shortcuts import render

def index(request):
    template = 'group/index.html'
    return render(request, template)

def group_posts(request, slug):
    template = 'group/index.html'
    return render(request, template)

