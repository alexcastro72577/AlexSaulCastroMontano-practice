from Inheritance.Classes.Land import Land


class Car(Land):
    def __init__(self, name, price, has_motor, use_gas):
        super().__init__(name, price, has_motor)
        self.__use_gas = use_gas

    def display_data(self, ):
        print(self.get_name() + str(self.get_price()) + self.has_motor+ self.__use_gas)
