from django.shortcuts import render
from .models import Atricles
# Create your views here.
def home(request):
    '''content is rendered dynamically onto the homepage.html of the app'''
    articles = Atricles.objects.all()
    return render(request,'articles/homepage.html', {'articles': articles})