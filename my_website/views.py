from django.shortcuts import render
from .models import Article

def home(request):
    article = Article.objects.filter(part=1).first()
    return render(request, 'index.html', {'article': article})

def page2(request):
    article = Article.objects.filter(part=2).first()
    return render(request, 'page2.html', {'article': article})