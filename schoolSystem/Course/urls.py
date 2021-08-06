from django.urls import path
from django.urls.resolvers import URLPattern
from .views import register_course

urlpatterns=[
    path("register/",register_course,name="register_course"),
]