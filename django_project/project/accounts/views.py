from django.shortcuts import render

# Create your views here.
def signup(request):
    '''directs to signup/login template'''
    return render(request, 'accounts/signup.html')