from django.db import models

class Task(models.Model):
    heading = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)
    date = models.DateField()
    is_deleted = models.CharField(max_length=2,default='n')
