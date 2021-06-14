from django.urls import path
from .views import home,getlocation
urlpatterns = [
    path('',home),
    path('loc/',getlocation)
]