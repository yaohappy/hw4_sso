from django.http import HttpResponse
from django.shortcuts import render

from .models import Order


def get_order(request):
    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        order_list = Order.objects.filter(customer=search_text).order_by('order_id').values('order_id', 'customer').distinct()
        return render(request, 'first_page.html', {
            'order_list': order_list,
        })
    else:
        return render(request, 'first_page.html')


def get_order_detail(request, order_id):
    item_list = Order.objects.filter(order_id=order_id)
    customer = item_list[0].customer
    return render(request, 'second_page.html', {
        'item_list': item_list,
        'order_id': order_id,
        'customer': customer,
    })


def ajax(request):
    search_text = request.GET.get('search_text')
    order_list = Order.objects.filter(
        customer=search_text
    ).order_by('order_id').values_list('order_id', flat=True).distinct()
    html = ""
    if len(order_list) == 0:
        html = "<tr><td colspan='2'>No Orders</td></tr>"
    else:
        for order in order_list:
            html = html + "<tr><td><a href='/order/{0}/'>{0}</a></td><td>{1}</td></tr>".format(order, search_text)
    return HttpResponse(html)
