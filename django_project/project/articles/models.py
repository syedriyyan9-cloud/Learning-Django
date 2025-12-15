from django.db import models

# Create your models here.
class Atricles(models.Model):
    '''a class to represent the table for articles inside the database'''
    title =  models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''make queryset return instances of model using its attribute value'''
        return self.title