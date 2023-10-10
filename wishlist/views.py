from django.shortcuts import render, redirect, get_object_or_404
from wishlist.wishlist import Wishlist
from artshop.models import Product
from django.conf import settings
from datetime import datetime
from django.views.decorators.http import require_POST

# Create your views here.
def wishlist(request):
    wishlist = Wishlist(request)
    return render(request, 'artshop/wishlist.html', {
        'wishlist': wishlist,
        
    })





@require_POST


def them_vao_wishlist(request, product_id):
    wishlist = Wishlist(request)
    product = get_object_or_404(Product, id=product_id)
    if request.POST.get('btnThemVaoWishlist' + str(product_id)):
        quantity = int(request.POST.get('quantity' + str(product_id)))
        wishlist.add(product, quantity)
    return redirect('wishlist:wishlist')


def xoa_san_pham_wishlist(request, product_id):
    wishlist = Wishlist(request)
    product = get_object_or_404(Product, id=product_id)
    wishlist.remove(product)
    return redirect('wishlist:wishlist')
