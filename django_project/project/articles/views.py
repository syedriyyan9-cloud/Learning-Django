from django.shortcuts import render

# Create your views here.
def home(request):
    '''renders homepage.html'''
    return render(request,'articles/homepage.html')