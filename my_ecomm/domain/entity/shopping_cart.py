from functools import reduce

from .interfaces.shopping_cart import IShoppingCart
from .product import IProduct


from my_ecomm.domain.entity.exceptions.shopping_cart import \
        QuantityGreaterThanItemQuantity


class ShoppingCartItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity


class ShoppingCart(IShoppingCart):
    def __init__(self,
                 uuid: str):
        self.uuid = uuid
        self.item_list = []

    def __len__(self):
        return reduce(lambda x, item: item.quantity + x, self.item_list, 0)

    def add_product(self, product: IProduct, quantity: int = 1):
        for item in self.item_list:
            if product == item.item:
                item.quantity += quantity
                return
        self.item_list.append(ShoppingCartItem(item=product,
                              quantity=quantity))

    def remove_product(self, product: IProduct, quantity: int):
        for item in self.item_list:
            if item.item is product:
                if quantity > item.quantity:
                    raise QuantityGreaterThanItemQuantity
                item.quantity -= quantity
                return
