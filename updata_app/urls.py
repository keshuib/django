from django.urls import path
from .views import *

urlpatterns=[

    path("updates/",UpateViews.as_view()),
    path("update/<int:id>/",UptateView.as_view())
]