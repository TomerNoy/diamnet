from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.cart_view, name='cart'),
    path('cart_add', views.cart_add_htmx, name='cart_add_htmx'),
    path('cart_del/<int:cart_id>/<int:jewl_id>/', views.cart_del_htmx, name='cart_del_htmx'),

]
