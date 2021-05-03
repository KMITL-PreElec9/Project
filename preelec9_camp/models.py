from django.db import models

class Staff_auth(models.Model):
    email = models.CharField(max_length=200)
    division = models.CharField(max_length=200) 
    def __str__(self):
        return self.email

class Campdata(models.Model):
    gender_choices = [
        ('นาย', 'นาย'),
        ('นางสาว', 'นางสาว'),
    ]
    religion_choices = [
        ('พุทธ', 'พุทธ'),
        ('คริสต์', 'คริสต์'),
        ('อิสลาม', 'อิสลาม'),
        ('อื่นๆ', 'อื่นๆ'),
    ]
    gender = models.CharField(choices=gender_choices, max_length=6, null=True)
    name = models.CharField(max_length=100,null=True)
    nickname = models.CharField(max_length=30,null=True)
    student_id = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    birth_date = models.DateField(null=True)
    religion = models.CharField(choices=religion_choices, max_length=6, null=True)
    allergic_foods = models.CharField(max_length=200, null=True)
    allergic_meds = models.CharField(max_length=200, null=True)
    congenital_disease =  models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=1000, null=True)
    self_telephone_num = models.CharField(max_length=10, null=True)
    parent_telephone_num = models.CharField(null=True,  max_length=10)
    line_id = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    passion = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    reg_useremail = models.EmailField(null = True)
    def __str__(self):
        return self.name