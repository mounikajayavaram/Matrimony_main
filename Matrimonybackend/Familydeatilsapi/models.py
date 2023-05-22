from django.db import models

# Create your models here.
class Familydetails(models.Model):
    Family_Values = models.CharField(max_length=150,null=False,blank=False)
    Family_Type = models.CharField(max_length=150,null=False,blank=False)
    Family_Status = models.CharField(max_length=150,null=False,blank=False)
    No_Of_Brothers = models.CharField(max_length=150,null=False,blank=False,default='null')
    No_Of_Brothers_Married = models.CharField(max_length=150,null=False,blank=False,default='null')
    No_Of_Sisters = models.CharField(max_length=150,null=False,blank=False,default='null')
    No_Of_Sisters_Married = models.CharField(max_length=150,null=False,blank=False,default='null')
    Mother_Tounge = models.CharField(max_length=150,null=False,blank=False)
    Father_Name = models.CharField(max_length=150,null=False,blank=False,default='null')
    Father_Occupation = models.CharField(max_length=150,null=False,blank=False,default='null')
    Mother_Name = models.CharField(max_length=150,null=False,blank=False,default='null')
    Mother_Occupation = models.CharField(max_length=150,null=False,blank=False,default='null')
    Family_wealth = models.CharField(max_length=150,null=False,blank=False,default='null')
    Relative_info = models.CharField(max_length=150,null=False,blank=False,default='null')
    About_Family = models.CharField(max_length=150,null=False,blank=False)