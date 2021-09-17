# from schoolSystem.Calendar.models import Calendar
# from schoolSystem.Course.models import Course
# from schoolSystem.Trainer.models import Trainer
# from schoolSystem.api import models
from django.db.models import fields
from rest_framework import  serializers
from student.models import Student
from Trainer.models import Trainer
from Course.models import Course
from Calendar.models import Calendar
class  StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields =("first_name","last_name","age",)

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields= ("first_name","last_name","salary",)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields= ("course_name","course_code","course_trainer",)

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model= Calendar
        fields= ("event_name","event_month","event_date",)

 
