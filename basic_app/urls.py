from django.conf.urls import url
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    # profile
    url(r'^profile/(?P<pk>\d+)/update/$', views.UserUpdateView.as_view(), name='user_update'),
    # addresses
    url(r'^address/new/$', views.address, name='address'),
    url(r'^address/(?P<pk>\d+)/update/$', views.AddressUpdateView.as_view(), name='address_update'),
    url(r'^address/(?P<pk>\d+)/delete/$', views.AddressDeleteView.as_view(), name='address_delete'),
    url(r'^addresses/list/$', views.AddressListView.as_view(), name='address_list'),

    # orders
    url(r'^order/new/$', views.order, name='order'),
    url(r'^order/(?P<pk>\d+)/delete/$', views.OrderDeleteView.as_view(), name='order_delete'),
    url(r'^order/list/$', views.OrderListView.as_view(), name='order_list'),
    url(r'^$', views.home, name='home'),
]
