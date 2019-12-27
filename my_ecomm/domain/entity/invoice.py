from enum import Enum
from typing import List

from .interfaces import IInvoice, IPayment, IProduct


class InvoiceEnum(Enum):
    NOT_PAID = 'NOT_PAID'
    PAID = 'PAID'
    PENDING = 'PENDING'


class Invoice(IInvoice):
    def __init__(self, items: List[IProduct], payment_method: IPayment,
                 freight: int, state: InvoiceEnum):
        pass
