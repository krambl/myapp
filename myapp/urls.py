from django.urls import path
from . import views

urlpatterns = [
    path('webpay/', views.webpay_list, name='webpay_list'),
    path('', views.post_list, name='post_list'),
]