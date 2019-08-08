from my_ecomm.domain.entity import Purchase


class TestPurchase:
    def test_add_payment_methods(self, order, payment):
        purchase = Purchase(order=order)

        purchase.set_payment_method(payment)

        assert purchase.payment_method is payment
