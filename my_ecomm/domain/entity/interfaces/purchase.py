from abc import ABC, abstractmethod

from .order import IOrder
from .payment import IPayment
from .address import IAddress


class IPurchase(ABC):
    uuid: str
    order: IOrder
    shipping_address: IAddress
    payment_method: IPayment
    status: str

    @abstractmethod
    def set_shipping_address(self, address: IAddress):
        pass

    @abstractmethod
    def set_payment_method(self, payment: IPayment):
        pass

    @abstractmethod
    def purchase(self):
        pass
