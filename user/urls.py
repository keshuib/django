from django.urls import path
from .views import *
urlpatterns = [
    path('login/',Userviewp.as_view()),
    path("regiser/",ResgisterView.as_view()),
    path("user/<int:id>/",UserView.as_view())
   
]