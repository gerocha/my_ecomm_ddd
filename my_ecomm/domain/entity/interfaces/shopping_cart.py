from typing import List
from abc import ABC, abstractmethod

from .product import IProduct
from .customer import ICustomer


class IShoppingCart(ABC):
    uuid: str
    customer: ICustomer
    item_list: List[IProduct]

    @abstractmethod
    def add_product(self, product: IProduct, quantity: int):
        raise Exception('Not implemented')

    @abstractmethod
    def remove_product(self, produtct: IProduct, quantity: int):
        raise Exception('Not implemented')

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def generate_order(self):
        pass
