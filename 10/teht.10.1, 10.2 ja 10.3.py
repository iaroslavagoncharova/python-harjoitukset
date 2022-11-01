class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            elif self.current_floor > target_floor:
                self.floor_down()
            else:
                self.current_floor = target_floor
        print(f'You have reached the {self.current_floor} floor')

    def floor_up(self):
        self.current_floor += 1
        print(f'The elevator is on the {self.current_floor} floor')

    def floor_down(self):
        self.current_floor -= 1
        print(f'The elevator is on the {self.current_floor} floor')


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        self.list_of_elevators = []
        for i in range(self.number_of_elevators):
            self.list_of_elevators.append(Elevator(self.bottom_floor, self.top_floor))

    def run_elevator(self, number_of_elevator, target_floor):
        self.list_of_elevators[number_of_elevator - 1].go_to_floor(target_floor)

    def fire_alarm(self):
        for i in self.list_of_elevators:
            i.go_to_floor(self.bottom_floor)


h = Elevator(1, 10)
h.go_to_floor(10)
h.go_to_floor(1)

building = Building(1, 10, 3)
building.run_elevator(1, 5)
building.run_elevator(2, 6)
building.run_elevator(3, 10)
building.fire_alarm()
