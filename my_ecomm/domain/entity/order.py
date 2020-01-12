from functools import reduce

from typing import List

from my_ecomm.domain.value_object.uuid import UUID
from my_ecomm.domain.entity.invoice import Invoice

from .interfaces import (IOrder, IProduct, IAddress, IPayment)


class Order(IOrder):
    def __init__(self, items: List[IProduct], uuid: UUID = None):
        self.uuid = uuid or UUID.new()
        self.items = items

    @property
    def total(self):
        return reduce(lambda total, product: product.price + total,
                      self.items, 0)

    def set_address(self, address: IAddress):
        self.address = address

    def set_payment(self, payment: IPayment):
        self.payment = payment

    def checkout(self):
        return Invoice(items=self.items,
                       payment_method=self.payment,
                       state='PENDING')
