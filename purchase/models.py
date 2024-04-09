from django.db import models
from django.contrib.auth.models import User
from gym.models import Plan
# Create your models here.
class Booking(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    plan=models.ForeignKey(Plan, on_delete=models.CASCADE)
    id_proof=models.ImageField(upload_to='id_proof')
    phone=models.CharField(max_length=15)