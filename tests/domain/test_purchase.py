from my_ecomm.domain.entity import Purchase, Invoice


class TestPurchase:
    def test_add_payment_methods(self, order, payment):
        purchase = Purchase(order=order)

        purchase.set_payment_method(payment)

        assert purchase.payment_method is payment

    def test_add_shipping_address(self, order, address):
        purchase = Purchase(order=order)

        purchase.set_shipping_address(address=address)

        assert purchase.shipping_address is address

    def test_purchase_total_should_generate_invoice(self, order):
        purchase = Purchase(order=order)

        invoice = purchase.purchase()

        assert isinstance(invoice, Invoice)
