from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50, default="None")
    email=models.EmailField(max_length=100, default="None")
    phone_number=models.IntegerField(max_length=10, default=0)
    location=models.CharField(max_length=50, default="None")
    skills=models.TextField(max_length=200, default="None")

    def __str__(self):
             return self.name
