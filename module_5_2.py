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

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floor}'

h1 = house('ЖК Эльбрус', 10)
h2 = house('ЖК Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))