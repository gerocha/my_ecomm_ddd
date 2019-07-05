from typing import NamedTuple, List


class IProductItem(NamedTuple):
    name: str
    quantity: str
    description: str
    price: int


class IProductList(NamedTuple):
    products: List[IProductItem]
