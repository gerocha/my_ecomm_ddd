from .invoice import Invoice
from .interfaces import (IPurchase, IOrder, IPayment, IAddress)


class Purchase(IPurchase):
    def __init__(self, order: IOrder):
        self.order = IOrder
        self.uuid = '1'
        self.shipping_address = None
        self.payment_method = None
        self.status = None
        self.total = self.order.total

    def purchase(self):
        if not self.payment_method:
            raise Exception('Missign payment method')

        return Invoice()

    def set_payment_method(self, payment: IPayment):
        self.payment_method = payment

    def set_shipping_address(self, address: IAddress):
        self.shipping_address = address
