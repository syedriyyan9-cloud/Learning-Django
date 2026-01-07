from django.shortcuts import render

from .models import Atricles

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
# Create your views here.
def home(request):
    """content is rendered dynamically onto the homepage.html of the app"""
    articles = Atricles.objects.all()
    # print(article)
    return render(request,'articles/homepage.html', {'articles': articles})

def article(request, slug):
    """searches for the template with same slug and then display it"""
    article = Atricles.objects.get(slug=slug)
    return render(request, 'articles/detail.html', {'article':article})

@login_required(login_url='/accounts/login/')
def articles_create(request):
    """renders the article create template"""
    return render(request,'articles/create.html')