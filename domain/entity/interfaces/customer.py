from typing import NamedTuple, Type, Callable, Any

from .address import IAddress

Address = Type[IAddress]


class ICustomer(NamedTuple):
    name: str
    email: str
    password: str
    address: Address

    setAddress: Callable[[Address], Any]
