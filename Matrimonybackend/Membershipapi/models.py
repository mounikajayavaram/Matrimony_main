from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class SilverPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    allowed_profiles = models.IntegerField(default=1)

class GoldPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    allowed_profiles = models.IntegerField(default=40)
    validity_period = models.IntegerField(default=3)

class PremiumPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    validity_period = models.IntegerField(default=3)

class DedicatedRMPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
