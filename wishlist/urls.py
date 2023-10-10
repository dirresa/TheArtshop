from django.urls import path
from wishlist.views import *

app_name = 'wishlist'
urlpatterns = [
     path('wishlist/', wishlist, name='wishlist'),
     path('xoa-san-pham-wishlist/<int:product_id>/', xoa_san_pham_wishlist, name='xoa_san_pham_wishlist'),
     path('them-vao-wishlist/<int:product_id>/', them_vao_wishlist, name='them_vao_wishlist'),
]

