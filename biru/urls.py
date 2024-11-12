from django.urls import path
from .views import testimoni, diskon

app_name = 'biru'

urlpatterns = [
    path('testimoni/', testimoni, name='testimoni'),
    path('diskon/', diskon, name='diskon'),

]