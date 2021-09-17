from django.db import models

# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=10)
    last_name= models.CharField(max_length=10)
    profile = models.ImageField(null= True, blank=True, upload_to="images/")
    gender = ((u"F",u"Female"),
               (u"M",u"Male"),
               (u"O",u"Other")    
    )
    gender = models.CharField(max_length=1,choices=gender)
    email = models.EmailField()
    bank_account = models.IntegerField()
    nationality = models.CharField(max_length=14)
    phone_Number= models.PositiveIntegerField()
    language = models.CharField(max_length=15)
    county = models.CharField(max_length=12)
    contract = models.FileField(null= True, blank=True, upload_to="images/")
    id_number = models.IntegerField()
    cv= models.FileField(null= True, blank=True, upload_to="images/")
    proffession= models.CharField(max_length=32)
    salary = models.PositiveBigIntegerField()
  
    def __str__(self):
        return self.first_name
    
