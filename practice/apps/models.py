from django.db import models
from django.contrib.auth.models import User
# Create your models here. 

class CustomUser(models.Model):
    user_id = models.CharField(max_length=50)
    user_pw = models.CharField(max_length=50)
    recommender = models.ForeignKey(User, on_delete=models.CASCADE, null=True)