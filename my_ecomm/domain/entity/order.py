from functools import reduce

from typing import List

from .interfaces import (IOrder, IProduct)


class Order(IOrder):
    def __init__(self, products: List[IProduct]):
        self.products = products
        self.uuid = ''

        @property
        def total(self):
            return reduce(lambda product, total: product.price + total,
                          self.products)
