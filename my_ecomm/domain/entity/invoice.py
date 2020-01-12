from enum import Enum
from typing import List

from .interfaces import IInvoice, IPayment, IProduct


class InvoiceEnum(Enum):
    NOT_PAID = 'NOT_PAID'
    PAID = 'PAID'
    PENDING = 'PENDING'


class Invoice(IInvoice):
    def __init__(self, items: List[IProduct], payment_method: IPayment,
                 state: InvoiceEnum):
        self.items = items
        self.payment_method = payment_method
        self.state = state

    def pay(self):
        self.payment_method.pay()
