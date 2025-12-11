from django.http import HttpResponse

from django.shortcuts import render

def about(request):
    '''function reponding to about url request'''
    # return HttpResponse('about page')
    return render(request, 'about.html')

def home(request):
    '''function responding to home url request'''
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')