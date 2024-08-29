from django.urls import path
from ola.views import*

app_name='travelling'
urlpatterns=[
    path('travel/',travel,name='travel'),
]
