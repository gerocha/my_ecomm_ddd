from my_ecomm.domain.entity.shopping_cart import ShoppingCart


class TestShoppingCart:
    def test_add_item_to_cart_should_add_item(self, product, customer):
        cart = ShoppingCart(customer=customer, uuid='1')
        cart.add_product(product=product)

        assert len(cart) == 1
