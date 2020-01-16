from my_ecomm.domain.entity.shopping_cart import ShoppingCart


class ShoppingCartService:

    @staticmethod
    def new():
        return ShoppingCart()

    @staticmethod
    def add_product(cart, product):
        cart.add_product(product)

    @staticmethod
    def remove_product(cart: ShoppingCart, product, quantity):
        cart.remove_product(product=product, quantity=quantity)

    @staticmethod
    def generate_order(cart: ShoppingCart):
        return cart.generate_order()
