from typing import List
from abc import ABC, abstractmethod

from .product import IProduct
from .payment import IPayment
from .address import IAddress


class IOrder(ABC):
    uuid: str
    items: List[IProduct]
    payment: IPayment
    address: IAddress

    @property
    def total(self):
        pass

    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def set_address(self, address: IAddress):
        pass

    @abstractmethod
    def set_payment(self, payment: IPayment):
        pass
