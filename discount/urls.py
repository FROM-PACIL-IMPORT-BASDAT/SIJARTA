from django.urls import path
from .views import *

app_name = 'discount'

urlpatterns = [
    path('', main, name='main'),
]