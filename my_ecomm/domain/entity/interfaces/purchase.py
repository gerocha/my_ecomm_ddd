from typing import NamedTuple, Type, Callable, Any

from .order import IOrder
from .product import IProduct
from .payment import IPayment
from .address import IAddress

Order = Type[IOrder]
Product = Type[IProduct]
Payment = Type[IPayment]
Address = Type[IAddress]


class IPurchase(NamedTuple):
    uuid: str
    order: Order
    shipping_address: Address
    payment: Payment
    status: str

    set_shipping_address: Callable[[Address], Any]
    set_payment: Callable[[Payment], Any]
    purchase: Callable[[], Any]
