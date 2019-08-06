from typing import List
from .interfaces.shopping_cart import IShoppingCart
from .product import IProduct

from .order import Order
from .customer import ICustomer


class ShoppingCart(IShoppingCart):
    def __init__(self,
                 uuid: str,
                 customer: ICustomer,
                 products: List[IProduct] = []):
        self.uuid = uuid
        self.products = products
        self.customer = customer
        self.order = None

    def __len__(self):
        return len(self.products)

    def add_product(self, product: IProduct):
        self.products.append(product)

    def remove_product():
        pass

    def generate_order(self):
        if self.order:
            return self.order

        order = Order(products=self.products)
        return order
