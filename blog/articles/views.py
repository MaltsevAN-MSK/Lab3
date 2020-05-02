from .models import Article
from django.shortcuts import render
from django.http import HttpResponse
from django import template

# Create your views here.

#def home(request):
#    return render (request, 'templates/index.html')
def archive(request):
    return render(request, 'templates/archive.html', {"posts":Article.objects.all()})
