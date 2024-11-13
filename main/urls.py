from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),  
    path('pengguna/', try_pengguna, name='try_pengguna'), 
    path('pekerja/', try_pekerja, name='try_pekerja'),
    
]