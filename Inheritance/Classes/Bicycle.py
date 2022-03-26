from Inheritance.Classes.Land import Land


class Bicycle(Land):

    def __init__(self, name, price, has_motor, exercise_bike):
        super().__init__(name, price, has_motor)
        self.__exerciseBike = exercise_bike

    def display_data(self, ):
        print(self.get_name() + str(self.get_price()) + self.has_motor+self.__exerciseBike)
