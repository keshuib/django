from django.urls import path
from .views import FreeCourseView

urlpatterns=[
    path('freecourse/',FreeCourseView.as_view())
]