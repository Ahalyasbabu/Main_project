from django.db import models
from departments.models import Departments

# Create your models here.
class Docotrs(models.Model):
    name = models.CharField(max_length=20)
    qualification = models.CharField(max_length=30)
    img = models.ImageField(upload_to='appUploads', default=None)
    availability = models.BooleanField()
    year_of_experience = models.IntegerField()
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)