class TestOrder:
    def test_add_item(self, order, product):
        order.add_item(product)

        assert len(order.items) == 1

    def test_remove_item(self, order, product):
        order.add_item(product)

        order.remove_item(item=product, quantity=1)

        assert len(order.item) == 0

    def test_set_payment(self, order, payment_credit_card):
        order.set_payment(payment_credit_card)

        assert order.payment is payment_credit_card

    def test_set_address(self, order, address):
        order.set_address(address)

        assert order.address is address
