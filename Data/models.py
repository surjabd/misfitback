from django.db import models

# Create your models here.

class acce_data(models.Model):
    device_id = models.CharField(max_length=10)
    data_x = models.CharField(max_length=3)
    data_y = models.CharField(max_length=3)
    data_z = models.CharField(max_length=3)
    data = models.DateTimeField(auto_now=True, blank=True, null=True)
