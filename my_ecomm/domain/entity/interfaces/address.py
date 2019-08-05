from typing import NamedTuple


class IAddress(NamedTuple):
    uuid: str
    city: str
    neighborhood: str
    state: str
    zipcode: str
