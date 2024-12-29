class house:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor > self.number_of_floor or new_floor <= 0:
            print(f'Такого этажа не существует!')
        else:
            for new_floor in range(1, new_floor + 1):
                print(new_floor)


h1 = house('ЖК Горский', 18)
h2 = house('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)