from django.db import models

# Create your models here.
class studentModel(models.Model):
    roll=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    father_name=models.CharField(max_length=30)
    address=models.TextField()
