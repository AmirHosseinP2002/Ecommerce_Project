from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_create_view, name='create'),
]