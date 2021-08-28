from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from store.models import Product, OrderItem


def say_hello(request):
    #limited = Product.objects.all()[1:5]
    #query_set = Product.objects.filter(inventory=F('collection__id'))
    # | Q(inventory__lt=10) | Q(unit_price__lt=20)
    #product = Product.objects.filter(pk=1).first()
    #query_values = Product.objects.values('id', 'title', 'collection__title')

    task = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(task)})
