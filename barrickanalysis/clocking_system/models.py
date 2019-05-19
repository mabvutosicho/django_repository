from django.db import models
from App_users.models import Users
from django.utils import timezone


# Create your models here.


class Clock_in(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now=True)
    
    
    

class Clock_out(models.Model):
    time_out = models.DateTimeField(auto_now=True)
    time_in_id = models.ForeignKey(Clock_in, on_delete=models.CASCADE, blank=True)
    
    

