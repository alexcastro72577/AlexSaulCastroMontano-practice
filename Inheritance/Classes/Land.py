from Inheritance.Classes.Transport import Transport


class Land(Transport):

    def __init__(self, name, price, has_motor):
        super().__init__(name, price)
        self.has_motor = has_motor

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def display_data(self):
        print( self.get_name() + str(self.get_price()) + self.has_motor)
