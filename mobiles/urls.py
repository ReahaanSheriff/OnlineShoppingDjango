from django.urls import path

from . import views

urlpatterns = [ 
    path('',views.home,name='home'),
    path('accessories',views.accessory,name='accessory'),
    path('py/<str:value>/', views.desc, name="desc"),
    path('addcart/<int:pid>/<str:type>/', views.addcart, name="addcart"),
    path('clearproduct/<int:pid>/<str:type>/', views.clearProd, name="clearProd"),
    path('clearcart', views.clearcart, name="clearcart"),
    path('mobiles',views.mobile,name='mobile'),
    path('contactus',views.contact,name='contact'),
    path('checkout',views.checkout,name='checkout'),
    path('cart',views.cart,name='cart'),
    path('cart/quantity',views.qtyChange,name='qtyChange'),
]