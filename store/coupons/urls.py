from django.urls import path

from . import views

app_name = 'coupons'

urlpatterns = [
    path('', views.apply_coupon, name='apply'),
]
