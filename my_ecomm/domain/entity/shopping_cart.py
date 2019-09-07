from typing import List
from .interfaces.shopping_cart import IShoppingCart
from .product import IProduct

from .order import Order


class ShoppingCart(IShoppingCart):
    def __init__(self,
                 uuid: str,
                 products: List[IProduct] = []):
        self.uuid = uuid
        self.products = products
        self.order = None

    def __len__(self):
        return len(self.products)

    def add_product(self, product: IProduct):
        self.products.append(product)

    def remove_product():
        pass

    def generate_order(self):
        if not self.order:
            self.order = Order(products=self.products)

        return self.order
