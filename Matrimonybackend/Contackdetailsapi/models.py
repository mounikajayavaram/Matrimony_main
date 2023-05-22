from django.db import models

# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=62322222222222222,null=False,blank=False)
    Mobile_Number = models.IntegerField()
    Alternative_Mobile_Number = models.CharField(max_length=62322222222222222,null=False,blank=False)
    Convinient_Time_To_Call = models.CharField(max_length=62322222222222222,null=False,blank=False)
    Email = models.EmailField(max_length=444444, blank=False, null=False)
    Show_Permanent_Address = models.CharField(max_length=62322222222222222,null=False,blank=False)
    Show_Working_Address = models.CharField(max_length=62322222222222222,null=False,blank=False)
    # Profile_Created_By = models.CharField(max_length=62322222222222222,null=False,blank=False)


