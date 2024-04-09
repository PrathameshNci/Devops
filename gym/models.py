from django.db import models

# Create your models here.
class Plan(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    price=models.IntegerField()

class Plan_features(models.Model):
    plan=models.ForeignKey(Plan, on_delete=models.CASCADE) 
    feature=models.CharField(max_length=50)   