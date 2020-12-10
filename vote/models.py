from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save


class Voter(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    first_name= models.CharField(max_length=20, null=True)
    last_name= models.CharField(max_length=20, null=True)
    birthday = models.IntegerField(default=18)
    email= models.EmailField(max_length=100)
    secure_pin=models.CharField(max_length=7, null=True)

@receiver(post_save, sender=User)
def creat_user_voter(sender, instance, created, **kwargs):
    if created:
        Voter.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_use_rvoter(sender,instance, **kwargs):
    instance.voter.save()



    
    
    

class Votes(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL,default=0, on_delete=models.CASCADE)
    vote= models.CharField(max_length=20)
    
    def __str__(self):
        return self.vote
    
# Create your models here.
