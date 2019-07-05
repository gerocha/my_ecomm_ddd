from typing import NamedTuple, List, Callable, Any, Type

from .product import IProduct
from .order import IOrder
from .address import IAddress
from .payment import IPayment

Address = Type[IAddress]
Order = Type[IOrder]
Product = Type[IProduct]
Payment = Type[IPayment]


class IShoppingCart(NamedTuple):
    uuid: str
    products: List[Product]
    address: Address
    payment: Payment

    addItem: Callable[[Product], Any]
    removeItem: Callable[[Product], Any]

    setAddress: Callable[[Address], Any]
    setPayment: Callable[[Payment], Any]

    checkout: Callable[[], Order]
