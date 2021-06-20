from django.shortcuts import render, redirect
from phones.models import Phone
from django.urls import reverse
from urllib.parse import urlencode
from phones.management.commands import import_phones


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    order_by = request.GET.get('sort', None)  # получаем переменную 'sort' (name, min_price, max_price)
    if order_by == 'min_price':  # параметр сортировки
        order = 'price'
    elif order_by == 'max_price':
        order = '-price'
    else:
        order = 'name'
    phones = list(Phone.objects.order_by(order))  # формируем список словарей из QuerySet

    context = {
        'data': phones,
    }
    return render(request, template, context)


def show_product(request, slug):  # slug получаем из адресной строки
    template = 'product.html'
    # получаем список всех 'slug', (единичных значений, а не кортежей (flat=true))
    slugs = Phone.objects.values_list('slug', flat=True)
    if slug in slugs:
        phone = Phone.objects.filter(slug=slug)[0]  # получаем строку из БД по полю slug
    else:
        return show_catalog(request)
    context = {'phone': phone}
    return render(request, template, context)


