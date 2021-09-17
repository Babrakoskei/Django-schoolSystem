from django.urls import path
from django.urls.resolvers import URLPattern
from .views import register_calendar,calendar_list

urlpatterns=[
    path("register/",register_calendar,name="register_calendar"),
     path("list/",calendar_list,name="calendar_list"),
]