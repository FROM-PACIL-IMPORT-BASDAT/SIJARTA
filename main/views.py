from django.shortcuts import render

def main(request):
    return render(request, 'landing_page.html')

def try_pengguna(request):
    return render(request, 'pengguna.html')

def try_pekerja(request):
    return render(request, 'pekerja.html')