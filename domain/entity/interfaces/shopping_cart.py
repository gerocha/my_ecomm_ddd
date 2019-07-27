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

    add_product: Callable[[Product], Any]
    remove_product: Callable[[Product], Any]

    generate_order: Callable[[], Order]
