from django.db import models

# Create your models here.
class BasicInformation(models.Model):
    Profile_Created_By = models.CharField(max_length=62322222222222222,null=False,blank=False)
    Marital_Status = models.CharField(max_length=62322222222222222,null=False,blank=False)
    Your_Religion = models.CharField(max_length=62322222222222222,null=False,blank=False)
    Your_Caste = models.CharField(max_length=62322222222222222,null=False,blank=False)
    Sub_Caste = models.CharField(max_length=62322222222222222,null=False,blank=False)
    Mobile_Number = models.CharField(max_length=62322222222222222,null=False,blank=False)
    About_Yourself = models.CharField(max_length=62322222222222222,null=False,blank=False)
    # my_field = models.CharField(max_length=50, blank=False, null=False)
    Name = models.CharField(max_length=444444, blank=False, null=False)
    Surname = models.CharField(max_length=4444444, blank=False, null=False)
    Email = models.EmailField(max_length=444444, blank=False, null=False)
    Gender = models.CharField(max_length=44444, blank=False, null=False)
    D_O_B = models.CharField(max_length=44444, blank=False, null=False)
    Mobile_Number = models.CharField(max_length=444444, blank=False, null=False)
    Height = models.CharField(max_length=444444, blank=False, null=False)
    Blood_Group = models.CharField(max_length=444444, blank=False, null=False)
    Age = models.CharField(max_length=444444, blank=False, null=False)