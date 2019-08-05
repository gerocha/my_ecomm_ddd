from my_ecomm.domain.entity.shopping_cart import ShoppingCart

from my_ecomm.domain.entity.customer import ICustomer


class TestShoppingCart:
    def generate_shopping_cart(self, customer, uuid='1'):
        return ShoppingCart(customer=customer, uuid=uuid)

    def test_basic_assertions(self, product, customer):
        cart = self.generate_shopping_cart(customer=customer)

        assert isinstance(cart.customer, ICustomer)
        assert cart.uuid == '1'

    def test_add_item_to_cart_should_add_item(self, product, customer):
        cart = self.generate_shopping_cart(customer=customer)
        cart.add_product(product=product)

        assert len(cart) == 1

        cart.add_product(product=product)
        assert len(cart) == 2
