from django.db import models


# Create your models here.
class EducationDetail(models.Model):
    Qualification = models.CharField(max_length=150,null=False,blank=False)
    # Education_Profession = models.CharField(max_length=150,null=False,blank=False)
    Occupation = models.CharField(max_length=150,null=False,blank=False)
    Occupation_Details = models.CharField(max_length=150,null=False,blank=False)
    Annual_Income = models.CharField(max_length=150,null=False,blank=False)
    Employed_in = models.CharField(max_length=150,null=False,blank=False)
    Working_Location = models.CharField(max_length=150,null=False,blank=False)
    Special_Cases = models.CharField(max_length=150,null=False,blank=False)
    Education_Details = models.CharField(max_length=150,null=False,blank=False, default='null')
    # Occupation_Details = models.CharField(max_length=150,null=False,blank=False)
    # Employed_in = models.CharField(max_length=150,null=False,blank=False)
    # Annual_Income = models.CharField(max_length=150,null=False,blank=False)
    Income_type = models.CharField(max_length=150,null=False,blank=False,default='null')
    Working_Hours = models.CharField(max_length=150,null=False,blank=False,default='null')
    Working_Location = models.CharField(max_length=150,null=False,blank=False)
    Height = models.CharField(max_length=150,null=False,blank=False,default='null')
    Weight = models.CharField(max_length=150,null=False,blank=False,default='null')
    Blood_Group = models.CharField(max_length=150,null=False,blank=False,default='null')
    Complexion = models.CharField(max_length=150,null=False,blank=False,default='null')