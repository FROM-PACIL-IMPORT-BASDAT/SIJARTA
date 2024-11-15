from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path('homepage/', homepage, name='homepage'),
    path("layanan/<str:sub>/", subkategori_layanan, name="subkategori_layanan"),
    path('my_order/', my_order, name='my_order'),
]