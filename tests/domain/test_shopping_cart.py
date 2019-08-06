from my_ecomm.domain.entity import (ICustomer, IOrder)


class TestShoppingCart:
    def test_basic_assertions(self, cart):
        assert isinstance(cart.customer, ICustomer)
        assert cart.uuid == '1'

    def test_add_item_to_cart_should_add_item(self, cart, product):
        cart.add_product(product=product)

        assert len(cart) == 1

        cart.add_product(product=product)
        assert len(cart) == 2

    def test_generate_order(self, cart, product):
        cart.add_product(product=product)
        order = cart.generate_order()

        assert isinstance(order, IOrder)
