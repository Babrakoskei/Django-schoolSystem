from django.urls import path
from django.urls.resolvers import URLPattern
from .views import register_calendar

urlpatterns=[
    path("register/",register_calendar,name="register_calendar"),
]