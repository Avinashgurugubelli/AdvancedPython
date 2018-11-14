from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, default='Bangalore')
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50, unique=True)
    picture = models.CharField(max_length=250)

    # def __str__(self):
    #     return 'Contact [id = {}, Name ={}, Email = {}, phone ={}, city ={}, picture ={}]'.format(

    #     )