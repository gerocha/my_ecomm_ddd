from typing import Type

from .interfaces.shopping_cart import IShoppingCart
from .product import IProduct

Product = Type[IProduct]


class ShoppingCart(IShoppingCart):
    _products = []

    def __len__(self):
        return len(self._products)

    def add_product(self, product: Product):
        self._products.append(product)

    def get_product_list(self):
        return self._products

    def remove_product():
        pass

    def generate_order():
        pass
