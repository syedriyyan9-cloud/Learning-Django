from django.http import HttpResponse

def about(request):
    '''function reponsing to about url request'''
    return HttpResponse('about page')

def home(request):
    '''function responsing to home url request'''
    return HttpResponse('homepage')