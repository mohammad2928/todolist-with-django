from django.db import models
import datetime 

# Create your models here.
class Task(models.Model):
    
    def __str__(self):
        return self.name 
        
    name = models.CharField(max_length=100) # title 
    priority = models.IntegerField(default=1) # a priority between 1-10 (1 is low and 10 is very high)
    creation_date = models.DateField(default=datetime.date.today()) # date of creation task
    end_date = models.DateField(default=datetime.date.today()) # expected time for ending the task
    status = models.IntegerField(default=0) # if 1, it has been done and otherwise is 0 (default).
    description = models.TextField(default="No description") # description about the task