from my_ecomm.domain.entity.invoice import Invoice, InvoiceEnum


class TestInvoice:
    def test_generate_invoice(self):
        invoice = Invoice()
        assert invoice.state == InvoiceEnum.NOT_PAID
        assert invoice.uuid
