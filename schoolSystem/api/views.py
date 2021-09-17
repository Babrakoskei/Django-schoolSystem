# from django.shortcuts import render
# from rest_framework import viewsets
# from rest_framework.serializers import Serializer
# from student.models import Student
# from Trainer.models import Trainer
# from Course.models import Course
# from Calendar.models import Calendar
# from .serializers import StudentSerializer
# from .serializers import TrainerSerializer
# from .serializers import TrainerSerializer
from django.shortcuts import render
from rest_framework import serializers, viewsets
# from .serializers import ForAllSerializer
from rest_framework.serializers import Serializer
from .serializers import StudentSerializer
from .serializers import TrainerSerializer
from .serializers import CourseSerializer
from .serializers import CalendarSerializer
from student.models import Student
from Trainer.models import Trainer
from Course.models import Course
from Calendar.models import Calendar



class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class TrainerViewSet(viewsets.ModelViewSet):
    queryset= Trainer.objects.all()
    serializer_class= TrainerSerializer
class CourseViewSet(viewsets.ModelViewSet):
    queryset= Course.objects.all()
    serializer_class= CourseSerializer
class CalendarViewSet(viewsets.ModelViewSet):
    queryset= Calendar.objects.all()
    serializer_class= CalendarSerializer
 
