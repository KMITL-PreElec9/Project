from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    datetime = models.DateTimeField('date published')
    def __str__(self):
        return self.subject
