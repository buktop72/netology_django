from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.conf import settings
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    ls_stations = []
    with open(settings.BUS_STATION_CSV, encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ls_stations.append(row)  




    page = int(request.GET.get('page', 1))
    elems_per_page = 10
    paginator = Paginator(ls_stations, elems_per_page)
    page_ = paginator.get_page(page)
    content = page_.object_list

    context = {
        'bus_stations': content,
        'page': page_,
    }
    return render(request, 'stations/index.html', context)
