from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_create_view, name='create'),
    path('<uuid:order_id>/pdf/', views.order_pdf, name='order_pdf'),
    path('list/', views.CustomerOrderListView.as_view(), name='customer_list'),
]
