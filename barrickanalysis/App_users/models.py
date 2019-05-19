from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.

class Users(models.Model):
    GENDER = (
        ('m','male'),
        ('f','female'),

    )
    user_id = models.CharField(max_length=40,primary_key=True)
    firstname = models.CharField(max_length =40)
    lastname = models.CharField(max_length =40)
    sex = models.CharField(max_length=1,choices=GENDER)
    DOB = models.DateField()

    class Meta:
        verbose_name_plural = "Appusers"

    def __str__(self):
        return self.user_id
    
    


    
