from django.urls import path
from .views import CreateOrderViews

urlpatterns=[
    path("orders/",CreateOrderViews.as_view())
]