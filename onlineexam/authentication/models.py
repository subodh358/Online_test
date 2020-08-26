from django.db import models
from django.contrib.auth.models import AbstractUser
 
 
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20)
    prn = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null= False, blank= False)

