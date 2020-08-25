from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

import datetime

from django.db import models
from django.utils import timezone



class Signup(models.Model):
    user_choices=(
        ('2','CONSUMER'),
         ('1','PROVIDER'),
         )
    user=models.CharField(max_length=240,choices=user_choices,default='1')
   # slug=models.TextField(default="this-is-new-slug")
    first_name=models.CharField(max_length=250)
    second_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=140,unique=True)
    password=models.CharField(max_length=250)


    def __str__(self):
        return self.first_name

