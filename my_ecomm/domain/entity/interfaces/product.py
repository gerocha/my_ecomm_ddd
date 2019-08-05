from typing import NamedTuple


class IProduct(NamedTuple):
    name: str
    quantity: str
    description: str
    price: int
