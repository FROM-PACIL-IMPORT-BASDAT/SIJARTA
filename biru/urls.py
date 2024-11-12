from django.urls import path
from .views import testimoni

app_name = 'biru'

urlpatterns = [
    path('testimoni/', testimoni, name='testimoni'),
]