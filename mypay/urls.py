from django.urls import path
from .views import *

app_name = 'mypay'

urlpatterns = [
    path('', main, name='main'),
]