from django.urls import path
from .views import *
urlpatterns=[

    path("courses/",CourseView.as_view()),
    path("stages/",StageView.as_view()),
    path('chapter/',ChapterView.as_view()),
    path("sections/",SectionView.as_view()),
    path("stage/<int:pk>/",StageAllView.as_view())

]