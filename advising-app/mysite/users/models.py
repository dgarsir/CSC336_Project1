from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    #additional fields go here bb
    CHOICES = ((0, 'Student'), (1, 'Faculty'), (2, 'Crystal'))
    user_type = models.IntegerField(choices=CHOICES)
    EMPLID = models.CharField(default='', max_length=8)