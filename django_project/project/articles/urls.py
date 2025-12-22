from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.home, name='list'),
    # first slug is path formatter, other is a variable, 
    # same name to be used in the associated function
    path('<slug:slug>/', views.article, name = 'detail'), 
]