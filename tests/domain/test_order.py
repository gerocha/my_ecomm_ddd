from my_ecomm.domain.entity.order import Order
from my_ecomm.domain.entity.interfaces.invoice import IInvoice


class TestOrder:
    def test_set_payment(self, order, payment):
        order.set_payment(payment)

        assert order.payment is payment

    def test_set_address(self, order, address):
        order.set_address(address)

        assert order.address is address

    def test_total(self, product):
        order = Order(items=[product, product])
        assert order.total == 2 * product.price

    def test_checkout(self, product, payment):
        order = Order(items=[product])
        order.set_payment(payment)

        invoice = order.checkout()

        assert isinstance(invoice, IInvoice)
