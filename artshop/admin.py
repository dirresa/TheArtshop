from django.contrib import admin
from artshop.models import Product
from datetime import datetime
from django.utils.html import format_html

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    exclude = ('name', 'viewed')                      
    list_display = ('e_name', 'e_price', 'e_viewed', 'e_category', 'e_image') 
    list_filter = ('name', 'price', 'viewed',)                                                       
    search_fields = ('name__contains',)      

    @admin.display(description="Product")
    def e_name(self, obj):
        return f'{obj.name}'
    
    @admin.display(description="Price")
    def e_price(self, obj):
        return '{:,}'.format(int(obj.price))
    
    
    @admin.display(description="Views")
    def e_viewed(self, obj):
        return f'{obj.viewed}'
    
    @admin.display(description="Category")
    def e_category(self, obj):
        return f'{obj.category}'
    
    @admin.display(description="Image")
    def e_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="width: 45px; height: 45px;" />')


admin.site.register(Product, ProductAdmin)                                                 # Thay thế / Đè ProductAdmin cho / lên Product
admin.site.site_header = 'TheArtshop Admin'
