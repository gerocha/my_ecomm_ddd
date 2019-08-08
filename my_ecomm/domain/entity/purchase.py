from .interfaces import (IPurchase, IOrder, IPayment)


class Purchase(IPurchase):
    def __init__(self, order: IOrder):
        self.order = IOrder
        self.uuid = '1'
        self.shipping_address = None
        self.payment_method = None
        self.status = None

    def purchase(self):
        pass

    def set_payment_method(self, payment: IPayment):
        self.payment_method = payment

    def set_shipping_address(self, address):
        pass
