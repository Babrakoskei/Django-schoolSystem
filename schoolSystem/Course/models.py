from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=30)
    course_code= models.IntegerField()
    course_syllabus= models.FileField(null= True, blank=True, upload_to="images/")
    course_trainer= models.CharField(max_length=30)
    course_duration= models.CharField(max_length=30)
    course_projects = models.CharField(max_length=100)
   
    
    def __str__(self):
        return self.course_name