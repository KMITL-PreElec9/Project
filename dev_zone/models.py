from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    datetime = models.DateTimeField('date published')
    def __str__(self):
        return self.subject

class Test_Campdata(models.Model):
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
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=30)
    student_id = models.IntegerField(null=True)
    email = models.EmailField()
    birth_date = models.DateField()
    religion = models.CharField(choices=religion_choices, max_length=6, null=True)
    allergic_foods = models.CharField(max_length=200, null=True)
    allergic_meds = models.CharField(max_length=200, null=True)
    congenital_disease =  models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=1000, null=True)
    self_telephone_num = models.IntegerField()
    parent_telephone_num = models.IntegerField(null=True)
    line_id = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    passion = models.TextField(null=True)
    def __str__(self):
        return self.name

