from django.contrib.auth.models import AbstractUser
from django.db import models 


class CustomUsers(models.Model):

    user=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username


  