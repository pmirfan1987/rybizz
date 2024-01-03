from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)  # create table Tablename(name varchar(239) )
    age = models.IntegerField() # (age int)
    email = models.CharField(max_length=100)
 