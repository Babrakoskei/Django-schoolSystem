from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=10)
    last_name= models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    profile = models.ImageField(null= True, blank=True, upload_to="images/")
    gender = ((u"F",u"Female"),
               (u"M",u"Male"),
               (u"O",u"Other")    
    )
    gender = models.CharField(max_length=1,choices=gender)
    email = models.EmailField()
    class_name = models.CharField(max_length=15)
    student_id = models.CharField(max_length=20)
    nationality = models.CharField(max_length=14)
    # medical_report = models.FileField()
    phone_Number= models.PositiveIntegerField()
    registration_number= models.PositiveSmallIntegerField()
    big_sister = models.CharField(max_length=10)
    mentor_name = models.CharField(max_length=10)
    room_number = models.CharField(max_length=12)
    regions = models.CharField(max_length=10)
    language = models.CharField(max_length=15)
    county = models.CharField(max_length=12)
    # Device__number= models.ForeignKey()
    emergency_Contact = models.PositiveIntegerField()
    
