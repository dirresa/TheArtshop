from django.urls import path
from artshop.views import *

app_name = 'artshop'

urlpatterns = [
     path('', trang_chu, name='trang_chu'),
     path('danh-muc/<int:pk>/', danh_muc, name='danh_muc'),
     path('chi-tiet-san-pham/<int:pk>', chi_tiet_san_pham, name='chi_tiet_san_pham'),
     path('tim-kiem/', tim_kiem, name='tim_kiem'),
     path('lien-he/', lien_he, name='lien_he'),
     path('about/', about, name='about'),
]    
