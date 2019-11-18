from django.contrib import admin
from .models import Student,Faculty,Income,Expenditure
# Register your models here.
admin.site.register(Student)
admin.site.register(Expenditure)
admin.site.register(Income)
admin.site.register(Faculty)