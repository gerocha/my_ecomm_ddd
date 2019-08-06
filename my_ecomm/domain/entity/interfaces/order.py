from typing import List
from abc import ABC

from .product import IProduct


class IOrder(ABC):
    uuid: str
    products: List[IProduct]
    total: int
