from django.urls import path
from zomoto.views import*

app_name='foodie'
urlpatterns=[
    path('food/',food,name='food'),
]