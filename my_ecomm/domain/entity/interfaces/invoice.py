from typing import List
from typing_extensions import Literal
from abc import ABC, abstractmethod

from .product import IProduct
from .payment import IPayment
from .address import IAddress


class IInvoice(ABC):
    items: List[IProduct]
    payment_method: IPayment
    address: IAddress
    freight: int
    state: Literal['ACTIVE', 'NOT_PAID', 'PAID', 'PROCESSING']

    @abstractmethod
    def pay(self):
        pass
