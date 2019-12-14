import pytest

from my_ecomm.domain.entity.exceptions.shopping_cart import \
        QuantityGreaterThanItemQuantity


class TestShoppingCart:
    def test_add_item_to_cart_should_add_item(self, cart, product):
        cart.add_product(product=product)

        assert len(cart) == 1

        cart.add_product(product=product)
        assert len(cart) == 2

    def test_remove_item_from_cart_should_remove_item(self, cart, product):
        cart.add_product(product)

        cart.remove_product(product=product, quantity=1)
        assert len(cart) == 0

    def test_remove_item_with_value_greater_than_quantity_in_cart(self, cart,
                                                                  product):
        cart.add_product(product)

        with pytest.raises(QuantityGreaterThanItemQuantity):
            cart.remove_product(product=product, quantity=2)
