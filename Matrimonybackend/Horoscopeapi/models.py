from django.db import models

# Create your models here.
class Horoscope(models.Model):
    Moon_Sign = models.CharField(max_length=150,null=False,blank=False)
    Star = models.CharField(max_length=150,null=False,blank=False)
    Hororscope_Match = models.CharField(max_length=150,null=False,blank=False)
    Manglik = models.CharField(max_length=150,null=False,blank=False)
    Shani = models.CharField(max_length=150,null=False,blank=False)
    Gotra = models.CharField(max_length=150,null=False,blank=False)
    Place_Of_Birth = models.CharField(max_length=150,null=False,blank=False)
    Place_Of_Country = models.CharField(max_length=150,null=False,blank=False)
    # Photograph = models.FileField(max_length=232222,null=False,blank=False)
    Hours = models.CharField(max_length=232222,null=False,blank=False)
    Minitues = models.CharField(max_length=232222,null=False,blank=False)
    Seconds = models.CharField(max_length=232222,null=False,blank=False)
    Am_Pm = models.CharField(max_length=232222,null=False,blank=False)