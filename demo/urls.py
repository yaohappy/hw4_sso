from django.conf.urls import patterns, url

from django.contrib import admin

from order.views import get_order, get_order_detail, ajax

admin.autodiscover()

urlpatterns = [
    url(r'^$', 'demo.views.index', name='index'),
    url(r'^attrs/$', 'demo.views.attrs', name='attrs'),
    url(r'^metadata/$', 'demo.views.metadata', name='metadata'),
    # url(r'^accounts/', include('users.urls', namespace='users')),
    url(r'^search$', get_order, name='get_order'),
    url(r'^order/(?P<order_id>\w+)/$', get_order_detail, name='get_order_detail'),
    url(r'^ajax$', ajax, name='ajax'),
    url(r'^admin/', admin.site.urls),
]