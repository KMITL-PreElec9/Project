from django.db import models

# Create your models here.
class Staff_auth(models.Model):
    email = models.CharField(max_length=200)
    division = models.CharField(max_length=200)