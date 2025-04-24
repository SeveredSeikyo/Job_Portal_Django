from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    company=models.CharField(max_length=100)
    role=models.CharField(max_length=150)
    qualification=models.CharField(max_length=150)
    description=models.TextField()
    experience=models.CharField(max_length=100)
    skills_required=models.CharField(max_length=250)
    salary=models.IntegerField()
    published_on=models.DateTimeField(auto_now_add=True)
