from django.urls import path
from .views import QuestionAppViews,AnswerView,QuestionViews,QuestionView,SectionQuestionView

urlpatterns=[
    path("questionapp/",QuestionAppViews.as_view()),
    path("answerview/",AnswerView.as_view()),
    path("questionviews/",QuestionViews.as_view()),
    path("questionview/<int:pk>/",QuestionView.as_view()),
    path("sectionques/",SectionQuestionView.as_view())

]