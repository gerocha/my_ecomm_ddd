from typing import List, Type
from abc import ABC, abstractmethod

from .product import IProduct
from .order import IOrder
from .address import IAddress
from .customer import ICustomer

Address = Type[IAddress]
Order = Type[IOrder]
Product = Type[IProduct]
Customer = Type[ICustomer]


class IShoppingCart(ABC):
    def __init__(self,
                 uuid: str,
                 customer: Customer,
                 products: List[Product] = []):
        self.uuid = uuid
        self.products = products
        self.customer = customer

    @abstractmethod
    def add_product(self, product: Product):
        raise Exception('Not implemented')

    @abstractmethod
    def remove_product(self, produtct: Product):
        raise('Not implemented')

    @abstractmethod
    def generate_order() -> Order:
        raise('Not implemented')
