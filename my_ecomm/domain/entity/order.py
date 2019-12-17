from functools import reduce

from typing import List

from .interfaces import (IOrder, IProduct)


class Order(IOrder):
    def __init__(self, uuid: str):
        self.uuid = uuid

        @property
        def total(self):
            return reduce(lambda product, total: product.price + total,
                          self.products)
