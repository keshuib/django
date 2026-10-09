from django.urls import path
from .views import TeacherView

urlpatterns=[
path("teachers/",TeacherView.as_view())


]