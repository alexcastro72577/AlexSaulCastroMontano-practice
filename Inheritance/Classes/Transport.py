from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        pass

    def get_price(self):
        pass
