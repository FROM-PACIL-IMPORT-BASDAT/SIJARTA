from django.shortcuts import render

def testimoni(request):
    return render(request, 'testimoni.html')

def diskon(request):
    return render(request, 'diskon.html')

def pembelian_voucher(request):
    return render(request, 'pembelian_voucher.html')