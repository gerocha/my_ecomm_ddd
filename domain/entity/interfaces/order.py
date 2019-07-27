from typing import NamedTuple, List, Type

from .product import IProduct

Product = Type[IProduct]


class IOrder(NamedTuple):
    uuid: str
    products: List[Product]
    total: int
