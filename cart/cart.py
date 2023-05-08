from product.models import Product

CART_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = self.request.session

        cart = self.session.get(CART_ID)
        if not cart:
            cart = self.session[CART_ID] = {}
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()

        for item in self.cart.values():
            product = Product.objects.get(pk=int(item['id']))
            item['product'] = product
            item['total'] = item['quantity'] * int(item['price'])

            yield item

    def make_unique_id(self, product_id, color, size):
        unique = f'{product_id}_{color}_{size}'

        return unique

    def add_to_cart(self, product, color, size, quantity):
        unique_id = self.make_unique_id(product.id, color, size)

        if unique_id not in self.cart:
            self.cart[unique_id] = {'quantity': 0, 'price': str(product.price), 'id': str(product.id), 'size': size,
                                    'color': color, 'unique_id': unique_id}
        self.cart[unique_id]['quantity'] += int(quantity)

        self.save()

    def delete_item(self, unique_id):
        if unique_id in self.cart:
            del self.cart[unique_id]
            self.save()

    def save(self):
        self.session.modified = True
