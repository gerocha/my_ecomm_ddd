class TestePurchase:
    def test_from_add_product_till_order_finish(self, product, cart, payment):
        cart.add_product(product)
        order = cart.generate_order()

        order.set_payment(payment)
        order.checkout()
