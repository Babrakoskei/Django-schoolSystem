from django.shortcuts import render
from student.models import Student
from Course.models import Course
from Trainer.models import Trainer
from Calendar.models import Calendar

def home(request):
    students= Student.objects.count()
    courses = Course.objects.count()
    trainers = Trainer.objects.count()
    calendar = Calendar.objects.count()
    data = {"students": students,"courses":courses,"trainers":trainers,"calendar": calendar}
    return render(request,"home.html",data)
