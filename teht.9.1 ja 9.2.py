import random


class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.max_speed = max_speed
        self.odometer = 0
        self.speed = 0

    def print_info(self):
        print(f'Auton {self.register_number} '
              f'huippunopeus on {self.max_speed} km/h, '
              f'matkamittari: {self.odometer} km, '
              f'tämänhetkinen nopeus: {self.speed} km/h')

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.max_speed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change < 0:
            self.speed = 0
        elif self.speed + speed_change > self.max_speed:
            self.speed = self.max_speed

    def print_speed(self):
        print(f'Auton {self.register_number} tämänhetkinen nopeus on {self.speed} km/h')

    def drive(self, hours):
        self.odometer = self.odometer + hours * self.speed

    def print(self):
        print()


car = Car('ABC-123', 142)
car.print_info()
car.accelerate(30)
car.accelerate(70)
car.print_speed()
car.accelerate(-200)
car.print_speed()
car.drive(1.5)
