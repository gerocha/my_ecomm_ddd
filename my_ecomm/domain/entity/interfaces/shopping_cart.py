from typing import List
from abc import ABC, abstractmethod

from .product import IProduct
from .order import IOrder
from .customer import ICustomer


class IShoppingCart(ABC):
    uuid: str
    customer: ICustomer
    products: List[IProduct]

    @abstractmethod
    def add_product(self, product: IProduct):
        raise Exception('Not implemented')

    @abstractmethod
    def remove_product(self, produtct: IProduct):
        raise Exception('Not implemented')

    @abstractmethod
    def generate_order() -> IOrder:
        raise Exception('Not implemented')
