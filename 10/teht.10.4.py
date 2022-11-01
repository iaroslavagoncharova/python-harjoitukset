import random


class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.max_speed = max_speed
        self.odometer = 0
        self.speed = 0
        self.wins = 0

    def accelerate(self, speed_change):
        self.speed += speed_change
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.max_speed:
            self.speed = self.max_speed

    def drive(self, hours):
        self.odometer = self.odometer + hours * self.speed

    def print_info(self):
        print(f"Car's {self.register_number} speed is {self.speed} km/h and distance is {self.odometer} km, the car "
              f"has won {self.wins} times")


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for a in self.cars:
            a.accelerate(random.randint(-10, 15))
            a.drive(1)

    def print_status(self):
        for a in self.cars:
            a.print_info()

    def has_the_race_finished(self):
        for x in self.cars:
            if x.odometer > self.distance:
                x.wins += 1
                return True
        return False

cars = []
for i in range(1, 11):
    x = random.randint(100, 200)
    car = Car(f'ABC-{i}', x)
    cars.append(car)

race = Race('Grand Demolition Derby', 8000, cars)
count = 0
while not race.has_the_race_finished():
    race.hour_passes()
    count += 1
    if count % 10 == 0:
        race.print_status()

race.print_status()