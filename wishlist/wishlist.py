# import json
from decimal import Decimal
from django.conf import settings
from artshop.models import Product


class Wishlist(object):
    def __init__(self, request):
        self.session = request.session
        wishlist = self.session.get(settings.WISHLIST_SESSION_ID)
        if not wishlist:
            wishlist = self.session[settings.WISHLIST_SESSION_ID] = {}
        self.wishlist = wishlist

    def __iter__(self):
        product_ids = self.wishlist.keys()
        products = Product.objects.filter(id__in=product_ids)

        wishlist = self.wishlist.copy()
        for product in products:
            wishlist[str(product.id)]['product'] = product

        for item in wishlist.values():
            item['price'] = Decimal(item['price'])
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.wishlist.values())
    
    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.wishlist:
            self.wishlist[product_id] = { 'quantity': quantity, 'price': str(product.price), 'coupon': '1'}
        # else:
        #     self.wishlist[product_id]['quantity'] += int(quantity)
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.wishlist:
            del self.wishlist[product_id]
            self.save()

    def clear(self):
        del self.session[settings.WISHLIST_SESSION_ID]
        self.save()

