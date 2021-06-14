from django.urls import path
from .views import home,getlocation,botrequest
urlpatterns = [
    path('',home),
    path('loc/',getlocation),
    path('bot/',botrequest)
]