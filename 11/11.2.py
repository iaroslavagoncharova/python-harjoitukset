class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.max_speed = max_speed
        self.odometer = 0
        self.speed = 0

    def drive(self, hours):
        self.odometer = self.odometer + hours * self.max_speed

    def print_info(self):
        print(f"Car's {self.register_number} distance is {self.odometer} km")


class ElecticCar(Car):
    def __init__(self, register_number, max_speed, battery_capacity):
        super().__init__(register_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, register_number, max_speed, tank_volume):
        super().__init__(register_number, max_speed)
        self.tank_volume = tank_volume


c1 = ElecticCar('ABC-15', 180, 52.5)
c1.drive(3)
c2 = GasolineCar('ACD-123', 165, 32.3)
c2.drive(3)
c1.print_info()
c2.print_info()
