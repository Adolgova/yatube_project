
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница')

def group_posts(request, posts):
    return HttpResponse('Список друзей')
