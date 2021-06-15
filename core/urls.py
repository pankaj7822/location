from django.urls import path
from .views import home,getlocation,botrequest,fakefb
urlpatterns = [
    path('',home),
    path('loc/',getlocation),
    path('bot/',botrequest),
    path('flogin/',fakefb)
]