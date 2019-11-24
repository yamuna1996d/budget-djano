from django.db import models
from datetime import datetime,date

# Create your models here.

GENDER=(
    ('M','MALE'),
    ('F','FEMALE'),
    ('O','OTHERS')
)

class Income(models.Model):
    incomeid=models.IntegerField()
    source=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    # amount=models.IntegerField()

class Expenditure(models.Model):
    exid=models.IntegerField()
    source=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    date = models.DateField()



class Student(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.CharField(max_length=10)
    address=models.TextField()
    course=models.CharField(max_length=20)
    gender=models.CharField(max_length=2,choices=GENDER,default='M')

class Faculty(models.Model):
    name=models.CharField(max_length=20)
    course=models.CharField(max_length=10)
    address=models.TextField()