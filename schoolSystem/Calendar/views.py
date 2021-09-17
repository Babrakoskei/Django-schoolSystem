from django.shortcuts import render
from .forms import CalendarRegistrationForm
from .models import Calendar

def register_calendar(request):
    if request.method=="POST":
        form= CalendarRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
         form = CalendarRegistrationForm()
    return render(request,"register_calendar.html",{"form": form})
    
def calendar_list(request):
    calendars = Calendar.objects.all()
    return render(request,"calendar_list.html",{"calendars": calendars})