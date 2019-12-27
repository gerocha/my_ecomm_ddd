from typing import List, Literal
from abc import ABC, abstractmethod

from .product import IProduct
from .payment import IPayment


class IInvoice(ABC):
    items: List[IProduct]
    payment_method: IPayment
    freight: int
    state: Literal['ACTIVE', 'NOT_PAID', 'PAID', 'PROCESSING']

    @abstractmethod
    def pay(self):
        pass
