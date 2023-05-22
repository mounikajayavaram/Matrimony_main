from django.db import models

# Create your models here.
import datetime
class Contact(models.Model):
    Mobile_Number = models.CharField(max_length=70)
    Email = models.EmailField(max_length=80)
    PhoneNumber = models.IntegerField()
    Message = models.CharField(max_length=150,null=False,blank=False)
    Subject = models.CharField(max_length=277777777)