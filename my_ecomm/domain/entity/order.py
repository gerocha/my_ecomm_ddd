from typing import List

from .interfaces import (IOrder, IProduct)


class Order(IOrder):
    def __init__(self, products: List[IProduct]):
        self.products = products
