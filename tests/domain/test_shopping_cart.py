class TestShoppingCart:
    def test_add_item_to_cart_should_add_item(self, cart, product):
        cart.add_product(product=product)

        assert len(cart) == 1

        cart.add_product(product=product)
        assert len(cart) == 2

    def test_remove_item_from_cart_should_remove_item(self, cart, product):
        cart.remove_product(product=product, quantity=2)
        assert len(cart) == 0

    def test_remove_item_with_value_greather_than_quantity_in_cart(self,
                                                                   cart,
                                                                   product):
        cart.remove_product(product=product, quantity=2)
        assert len(cart) == 0
