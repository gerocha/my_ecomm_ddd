from my_ecomm.domain.entity.interfaces import IAddress


class User:
    def __init__(self, name: str, email: str, password: str,
                 address: IAddress = None):
        self.name = name
        self.email = email
        self.password = password
        self.address = address

    def new(self):
        if not self.name | self.email | self.password:
            raise "Missing fields"

