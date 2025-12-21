from django.shortcuts import render

from .models import Atricles

from django.http import HttpResponse
# Create your views here.
def home(request):
    '''content is rendered dynamically onto the homepage.html of the app'''
    articles = Atricles.objects.all()
    print(article)
    return render(request,'articles/homepage.html', {'articles': articles})

def article(request, slug):
    '''display the slug that is present in the url'''
    return HttpResponse(slug)
