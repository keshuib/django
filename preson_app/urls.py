from django.urls import path
from .views import PresonViews,UserSectionViews,Orderviews
urlpatterns=[

    path("personviews/",PresonViews.as_view()),
    path("usersectionviews/",UserSectionViews.as_view()),
    path("orders/",Orderviews.as_view())

]