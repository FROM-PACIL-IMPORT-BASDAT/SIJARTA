from django.shortcuts import render
import datetime

#  @login_required(login_url='/login')
def homepage(request):
    data = {
        'kategori1' : ['sub11', 'sub12'],
        'kategori2' : ['sub21'],
        'kategori3' : ['sub31', 'sub32', 'sub33']
    }
    filter = data
    filter_kat = request.GET.get('kategori')
    filter_sub = request.GET.get('subkategori')
    if filter_kat:
        data = {key: value for key, value in data.items() if filter_kat in key.lower()}
    if filter_sub:
        data = {
        key: [item for item in value if filter_sub.lower() in item.lower()]
        for key, value in data.items()
    }
    context = {'data' : data, 'filter':filter}

    return render(request, "homepage.html", context)

#  @login_required(login_url='/login')
def subkategori_layanan(request, sub):
    today = datetime.date.today()
    metode = ['Metode1', 'Metode2', 'Metode3']

    data = {
        'subkategori' : sub,
        'date' : today,
        'metode' : metode,
    }

    return render(request, "subkategori_layanan.html", data)

#  @login_required(login_url='/login')
def my_order(request):
    subkategori = ['sub11', 'sub12', 'sub21', 'sub31', 'sub32', 'sub33']
    status = ['Menunggu Pembayaran', 'Mencari Pekerja Terdekat', 'Pesanan Selesai']
    filter_sub = subkategori
    filter_stat = status

    if request.GET.get('subkategori'):
        subkategori = [request.GET.get('subkategori')]
    if request.GET.get('status'):
        status = [request.GET.get('status')]

    data = {
        'subkategori' : subkategori,
        'status' : status,
        'filter_sub' : filter_sub,
        'filter_stat' : filter_stat,
    }

    return render(request, "my_order.html", data)