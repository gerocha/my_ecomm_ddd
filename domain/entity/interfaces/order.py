from typing import NamedTuple, List, Type, Callable, Any

from .address import IAddress
from .product import IProduct
from .payment import IPayment

Address = Type[IAddress]
Product = Type[IProduct]
Payment = Type[IPayment]


class IOrder(NamedTuple):
    uuid: str
    products: List[Product]
    total: int
    shipping_cost: int
    address: Address
    payment: Payment
    status: str

    change_status: Callable[[str], Any]
