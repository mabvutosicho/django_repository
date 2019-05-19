from django.db import models

# Create your models here.
from clocking_system.models import Clock_out
from App_users.models import Users


class Vibration(models.Model):

    clock_out_id = models.ForeignKey(Clock_out, default=0,on_delete=models.SET_DEFAULT)
    duration = models.FloatField(max_length=200, default=0.0)
    vibration_Ve = models.FloatField(default=0.0)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    
