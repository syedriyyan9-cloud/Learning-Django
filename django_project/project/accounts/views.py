from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signup(request):
    '''directs to signup/login template'''
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', {"form":form})