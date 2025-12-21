from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # first slug is path formatter, other is a variable, 
    # same name to be used in the associated function
    path('<slug:slug>/', views.article), 
]