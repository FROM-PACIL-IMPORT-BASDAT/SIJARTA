from django.shortcuts import render

def testimoni(request):
    return render(request, 'testimoni.html')

def diskon(request):
    return render(request, 'diskon.html')