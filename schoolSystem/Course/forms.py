from django import forms
from django.db.models.base import Model
from .models import Course
class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model= Course
        fields= "__all__"