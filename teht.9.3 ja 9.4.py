import random


class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.max_speed = max_speed
        self.odometer = 0
        self.speed = 0

    def accelerate(self, speed_change):
        self.speed += speed_change
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.max_speed:
            self.speed = self.max_speed

    def drive(self, hours):
        self.odometer = self.odometer + hours * self.speed

    def print_info(self):
        print(f'Auton {self.register_number} nopeus on {self.speed} km/h ja matka on {self.odometer} km')

    def __lt__(self, other):
        return self.odometer > other.odometer



cars = []
for i in range(1, 11):
    x = random.randint(100, 200)
    car = Car(f'ABC-{i}', x)
    cars.append(car)

distance = False
while not distance:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.odometer >= 10000:
            distance = True

cars.sort()
for i in cars:
    i.print_info()
