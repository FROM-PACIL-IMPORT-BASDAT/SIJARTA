from django.urls import path
from .views import testimoni, diskon, pembelian_voucher

app_name = 'biru'

urlpatterns = [
    path('testimoni/', testimoni, name='testimoni'),
    path('diskon/', diskon, name='diskon'),
    path('pembelian_voucher/', pembelian_voucher, name='pembelian_voucher'),


]