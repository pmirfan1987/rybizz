from django.db import models


class Student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    DOB = models.DateField(max_length=30,blank=True, default='', null=True)
    
# Create your models here.
