class House:
    houses_history = []    # хранитеоь названия созданных объектов.

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)    # новый объект
        args = args[0]
        cls.houses_history.append(args)   #  Название объекта добавлялось в список houses_history
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor:int):
        if 0 < new_floor <= self.number_of_floors:
            for i in range(1, new_floor +1):
                print(i)
        else:
                print("Такого этажа не существует")

    def __len__(self):
         return self.number_of_floors
    def __str__(self):
        return  f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


    def __eq__(self, other):     # метод сравнения на равенство
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):     # метод сравнения "меньше чем"
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):      # метод сравнения "меньше или равно"
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):      # метод сравнения "больше чем"
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):      # метод сравнения "больше или равно"
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):      # метод сравнения "на неравенство"
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):     # метод "добавления элемента в множество"
        if isinstance(value, int):
             self.number_of_floors += value
             return self

    def __radd__(self, value):     # метод "симметричного сложения"
        return self.__add__(value)

    def __iadd__(self, value):     # метод "сложения с присвоением +="
        return self.__add__(value)

    def __del__(self):
        print( f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House("ЖК Матрёшки", 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
