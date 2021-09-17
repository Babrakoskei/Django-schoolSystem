from django.db import models

# Create your models here.
class Calendar(models.Model):
   event_name = models.CharField(max_length=80,null= True)
   event_month = models.CharField(max_length=20)
   event_date = models.DateTimeField(null= True)
   event_time = models.TimeField(null=True)
   event_organizer= models.CharField(max_length=15)
   event_venue = models.CharField(max_length=16)
   event_duration = models.DurationField(null=True)
   event_goal = models.CharField(max_length=200)
   event_approved_by = models.CharField(max_length=20)

   def __str__(self):
        return self.event_name
