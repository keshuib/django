from django.urls import path
from .views import RoutationCharView,FeatureView
urlpatterns=[
    path("routationchar/",RoutationCharView.as_view()),
    path("feature/",FeatureView.as_view())

]