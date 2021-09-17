from django.db import router
from django.urls import path,include
from rest_framework import routers,urlpatterns
from .views import StudentViewSet
from .views import TrainerViewSet
from .views import CourseViewSet
from .views import CalendarViewSet
router=routers.DefaultRouter()
router.register("student/",StudentViewSet)
router.register("Trainer/",TrainerViewSet)
router.register("Course/",CourseViewSet)
router.register("Calendar/",CalendarViewSet)
urlpatterns=[
    path("",include(router.urls)),
    path("",include(router.urls)),
    path("",include(router.urls)),
    path("",include(router.urls))
]