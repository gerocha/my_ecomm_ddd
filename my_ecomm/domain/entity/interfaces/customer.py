from typing import Type

from .address import IAddress

Address = Type[IAddress]


class ICustomer(object):
    def __init__(self, name: str, email: str, password: str, address: Address):
        self.name = name
        self.email = email
        self.password = password
        self.address = address

    def setAddress(address: Address):
        raise('Not implemented')
