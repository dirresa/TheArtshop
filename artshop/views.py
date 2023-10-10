from django.shortcuts import render, reverse, redirect, get_object_or_404
from artshop.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  
from cart.cart import Cart
from wishlist.wishlist import Wishlist
from django.http import JsonResponse  
from rest_framework import viewsets, permissions
from artshop.serializers import ProductSerializer
from cart.views import them_vao_gio_hang
from wishlist.views import them_vao_wishlist
from urllib.parse import urlencode
from django.conf import settings
from artshop.forms import *

# Create your views here.

categories = Category.objects.all()



def trang_chu(request):
    cart = Cart(request)

    # Sản phẩm nổi bật
    most_viewed_products = Product.objects.order_by('-viewed')[:10]

    return render(request, 'artshop/index.html', {
        'categories': categories,
        'most_viewed_products': most_viewed_products,
        'cart': cart,

    })


def danh_muc(request, pk):
    # Giỏ hàng
    cart = Cart(request)
    
    
    if pk == 0:         # Đọc tất cả sản phẩm
        products = Product.objects.order_by('name')
        title_category = f'All Products ({len(products)})'
    else:              
        products = Product.objects.filter(category=pk).order_by('name')
        title_category = f'{Category.objects.get(pk=pk)} ({len(products)})'


    # Lọc giá
    range_gia = ''
    tu_khoa = ''
    if request.GET.get('gia'):
        range_gia = request.GET.get('gia')
        # print(range_gia)
        tu_gia, den_gia = range_gia.split('-')
        tu_khoa = request.GET.get('tu_khoa').strip()

        if pk == 0:
            if den_gia != '':
                products = Product.objects.filter(price__gte=tu_gia, price__lt=den_gia).order_by('name')
                if tu_khoa != '':
                    products = Product.objects.filter(price__gte=tu_gia, price__lt=den_gia, name__contains=tu_khoa).order_by('name')
            else:
                products = Product.objects.filter(price__gte=tu_gia).order_by('name')
                if tu_khoa != '':
                    products = Product.objects.filter(price__gte=tu_gia, name__contains=tu_khoa).order_by('name')


        else:
            products = Product.objects.filter(category=pk, price__gte=tu_gia).order_by('name')
            if den_gia  != '':
                products = Product.objects.filter(category=pk, price__gte=tu_gia, price__lt=den_gia).order_by('name')
                if tu_khoa != '':
                    products = Product.objects.filter(category=pk, price__gte=tu_gia, price__lt=den_gia, name__contains=tu_khoa).order_by('name')

        title_category = f'Found {len(products)} products'
    
    # Phân trang
    products_per_page = 12
    page = request.GET.get('trang', 1)
    paginator = Paginator(products, products_per_page)
    try: 
        products_pager = paginator.page(page)
    except PageNotAnInteger:
        products_pager = paginator.page(1)
    except EmptyPage:
        products_pager = paginator.page(paginator.num_pages)
    

    return render(request, 'artshop/shop.html', {
        'categories': categories, 
        'products': products,
        'products_pager': products_pager,               
        'cart': cart,
        'range_gia': range_gia,                     
        'keyword': tu_khoa,
        'title_category': title_category,
    })
    






def chi_tiet_san_pham(request, pk):

    # Chi tiết sản phẩm
    product = Product.objects.get(pk=pk)

    # Sản phẩm liên quan
    related_products = Product.objects.filter(category=product.category.pk).exclude(pk=pk).order_by('name')[:20]

    # Thêm vào giỏ hàng
    quantity = 1
    if request.POST.get('btnThemVaoGioHang'):
        quantity = int(request.POST.get('quantity'))
        print(quantity)
        them_vao_gio_hang(request, pk, quantity)


    # Load thông tin giỏ hàng
    cart = Cart(request)

    # Thống kê số lượt xem
    product.viewed += 1
    product.save()

    return render(request, 'artshop/shop-detail.html', {
        'cart': cart,
        'categories': categories,
        'product': product,
        'related_products': related_products,
        'quantity': quantity,
        

    })

def tim_kiem(request):
    # Giỏ hàng
    cart = Cart(request)

    # Tìm kiếm
    products = []
    keyword = ''
    if request.GET.get('tu_khoa'):
        keyword = request.GET.get('tu_khoa').strip()
        products = Product.objects.filter(name__contains=keyword).order_by('name')
        # print(products)
    title_category = f'Found {len(products)} products'

     # Lọc giá
    if request.GET.get('gia'):
        range_gia = request.GET.get('gia')
        keyword = request.GET.get('tu_khoa').strip()
        base_url = reverse('artshop:danh_muc', kwargs={'pk': 0})
        query_string = urlencode({'gia': range_gia, 'tu_khoa': keyword})
        url = f'{base_url}?{query_string}'
        return redirect(url)


    # Phân trang
    products_per_page = 12
    page = request.GET.get('trang', 1)
    paginator = Paginator(products, products_per_page)
    try:
        products_pager = paginator.page(page)
    except PageNotAnInteger:
        products_pager = paginator.page(1)
    except EmptyPage:
        products_pager = paginator.page(paginator.num_pages)


    return render(request, 'artshop/shop.html', {
        'cart': cart,
        'categories': categories,
        'products_pager': products_pager,
        'title_category': title_category,
        'keyword': keyword,
    })


def lien_he(request):
    cart = Cart(request)

    ket_qua_lien_he = ''
    form = FormContact()
    if request.POST.get('btnSend'):
        form = FormContact(request.POST, Contact)
        if form.is_valid():
            request.POST._mutable = True
            post = form.save(commit=False)
            post.name = form.cleaned_data['name']
            post.email = form.cleaned_data['email']
            post.subject = form.cleaned_data['subject']
            post.message = form.cleaned_data['message']
            post.save()

        ket_qua_lien_he = '''
                <div class="alert alert-success" role="alert">
                    Your message has been sent! Thank you!
                </div>
                '''
    return render(request, 'artshop/contact-us.html', {
        'cart': cart,
        'form': form,
        'ket_qua_lien_he': ket_qua_lien_he,
    })

def about(request):
    cart = Cart(request)
    return render(request, 'artshop/about.html', {
        'cart': cart
    })


