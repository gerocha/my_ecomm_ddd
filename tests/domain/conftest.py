import pytest

from my_ecomm.domain.entity.product import Product
from my_ecomm.domain.entity.customer import Customer


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
