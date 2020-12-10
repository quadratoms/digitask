from django.db import models
from django.contrib.auth.models import User
from django.conf import settings




class Voter(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    email= models.EmailField(max_length=100)
    birthday = models.IntegerField(default=18)
    secure_pin=models.CharField(max_length=7)
    
    
    
    
    

class Votes(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL,default=0, on_delete=models.CASCADE)
    vote= models.CharField(max_length=20)
    
    def __str__(self):
        return self.vote
    
# Create your models here.
