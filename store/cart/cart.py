from decimal import Decimal

from django.contrib import messages
from django.utils.translation import gettext as _

from store.products.models import Product
from store.coupons.models import Coupon


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            self.session['cart'] = {}
            cart = self.session['cart']

        self.cart = cart

        self.coupon_id = self.session.get('coupon_id')

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': int(product.stock_records.first().final_price)}

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        messages.success(self.request, _('Product successfully added to cart'))

        self.save()

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]

            messages.success(self.request, _('Product successfully removed from cart'))

            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def save(self):
        self.session.modified = True

    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            
            except Coupon.DoesNotExist:
                pass
        
        return None
    
    def get_discount(self):
        if self.coupon:
            return round((self.coupon.discount / Decimal(100)) * self.get_total_price(), 0)
        
        return Decimal(0)
    
    def get_total_price_after_discount(self):
        return round(self.get_total_price() - self.get_discount(), 0)
