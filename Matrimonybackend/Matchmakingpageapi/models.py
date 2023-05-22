from django.db import models
from profileapi.models import Profile

# Create your models here.
class Matchmaking(models.Model):
    name = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    age = models.IntegerField(null = True, blank = True, default = None)
    gender = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    religion = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    caste = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    height = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    occupation = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    income = models.IntegerField(null = True, blank = True, default = None)
    D_O_B= models.CharField(max_length=222222222, null = True, blank = True, default = None)
    Mother_Tonge= models.CharField(max_length=222222222, null = True, blank = True, default = None)
    Education= models.CharField(max_length=222222222, null = True, blank = True, default = None)
    Location =models.CharField(max_length=222222222, null = True, blank = True, default = None)
    Hobbies=models.CharField(max_length=222222222, null = True, blank = True, default = None)
    Intersts=models.CharField(max_length=222222222, null = True, blank = True, default = None)
    Siblings=models.CharField(max_length=222222222, null = True, blank = True, default = None)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True, blank = True, default = None)
    




    
