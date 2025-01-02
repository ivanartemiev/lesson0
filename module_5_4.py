class house:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor > self.number_of_floor or new_floor <= 0:
            print(f'Такого этажа не существует!')
        else:
            for new_floor in range(1, new_floor + 1):
                print(new_floor)

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floor}'

    def __eq__(self, other):
        if isinstance(other, house):
            return self.number_of_floor == other.number_of_floor

    def __lt__(self, other):
        if isinstance(other, house):
            return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        if isinstance(other, house):
            return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other):
        if isinstance(other, house):
            return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        if isinstance(other, house):
            return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        if isinstance(other, house):
            return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floor += value
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floor += value
        return self


h1 = house('ЖК Эльбрус', 10)
print(house.houses_history)
h2 = house('ЖК Акация', 20)
print(house.houses_history)
h3 = house('ЖК Матрёшки', 20)
print(house.houses_history)

# Удаление объектов
del h2
del h3

print(house.houses_history)
