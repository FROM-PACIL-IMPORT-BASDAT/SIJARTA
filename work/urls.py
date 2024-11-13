from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path('', main, name='main'),
    path('my_work', my_work, name='my_work'),
]