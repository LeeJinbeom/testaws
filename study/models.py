from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    reg_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)