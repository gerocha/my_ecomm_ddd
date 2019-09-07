import pytest

from my_ecomm.domain.entity import (Product, Customer, ShoppingCart,
                                    Order, Payment, Address)


@pytest.fixture
def product():
    return Product(
            name='produto',
            quantity=4,
            description='descrevendo',
            price=10000
            )


@pytest.fixture
def customer():
    return Customer(
            name='batman',
            email='batman@batmail.batcom',
            password='batmandesnudo',
            address='caverna'
            )


@pytest.fixture
def cart(customer):
    return ShoppingCart(uuid='1')


@pytest.fixture
def order(product):
    return Order(products=[product])


@pytest.fixture
def payment():
    return Payment()


@pytest.fixture
def address():
    return Address(
            uuid='1',
            city='gothan',
            neighborhood='sei la',
            state='of panic',
            zipcode='111111111'
            )
