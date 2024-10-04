from django.db import models
class Employee(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Salary = models.FloatField()
    Email = models.CharField(max_length=30)
# Create your models here.
