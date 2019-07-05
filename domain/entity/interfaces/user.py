from typing import NamedTuple


class IUser(NamedTuple):
    name: str
    email: str
    password: str
