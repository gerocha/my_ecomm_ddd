from abc import ABC


class IPayment(ABC):
    uuid: str
    name: str
