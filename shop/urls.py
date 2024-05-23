from django.urls import path
from . import views, views_cart
from . import views_auth
from . import views_cabinet


app_name = 'shop'
urlpatterns = [
    path('', views.main, name='main'),
    path('detail/<int:pk>/', views.detail, name='detail'),


    path('add_product/', views.add_product, name='add_product'),

    path('delete_product/<int:product_id>/',views.delete_product, name='delete_product'),


    path('edit_product/<int:product_id>/',views.edit_product,name='edit_product'),


    path('admin_panel/',views.admin_panel,name='admin_panel'),


    path('cabinet/<str:username>/', views_cabinet.cabinet_views, name='cabinet'),

    path('create_order_cart/<str:username>/', views_cabinet.create_order_card, name='create_order_cart'),

    path('order/', views_cart.order, name='order'),


    path('delete_cartItem/<str:username>/<int:cart_id>/', views_cabinet.delete_from_cabinet_cart, name='delete_cartItem'),


    path('subscribe_product/<int:pk>/<str:username>/', views.subscribe_product, name='subscribe_product'),

    path('unsubscribe_product/<int:pk>/<str:username>/', views.unsubscribe_product, name='unsubscribe_product'),


    path('add_to_cart/<str:username>/<int:product_id>/', views_cart.add_to_cart, name='add_to_cart'),



    path('signup/', views_auth.signup, name='signup'),
    path('login/', views_auth.login, name='login'),
    path('logout/', views_auth.logout, name='logout'),
]