from typing import Type

from .interfaces.shopping_cart import IShoppingCart
from .product import IProduct

Product = Type[IProduct]

class ShoppingCart(IShoppingCart):
    products = []

    def __len__(self):
        return len(self.products)

    def add_product(self, product: Product):
        self.products.append(product)

    def generate_order():
        pass

    def remove_product():
        pass
