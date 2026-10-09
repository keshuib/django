from django.urls import path
from .views import PlabView,ClassTypeListView

urlpatterns=[
    path("plan/",PlabView.as_view()),
      path('class_type/',ClassTypeListView.as_view()),
]