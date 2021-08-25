from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
    query_set = Product.objects.filter(inventory=F('collection__id'))
    # | Q(inventory__lt=10) | Q(unit_price__lt=20)
    #product = Product.objects.filter(pk=1).first()

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(query_set)})
