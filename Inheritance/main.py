from Classes.Land import Land
from Classes.Car import Car
from Classes.Bicycle import Bicycle

if __name__ == "__main__":
    land1: Land = Land("Auto", 100, "Turbo")
    land2: Car = Car("Toyota", 100, "4x4", "T")
    land3: Bicycle = Bicycle("BMX", 100, "N/A", "T")
    land1.display_data()
    land2.display_data()
    land3.display_data()

