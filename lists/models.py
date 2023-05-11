from django.db import models


# Create your models here.

class Task(models.Model):
       ID = models.AutoField(primary_key=True)
       task = models.CharField(max_length=122)
       ddate = models.DateField()

       def __str__(self):
         return self.task
            
            
            
