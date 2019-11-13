from django.db import models

# Create your models here.

GENDER=(
    ('M','MALE'),
    ('F','FEMALE'),
    ('O','OTHERS')
)

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