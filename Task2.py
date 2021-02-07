from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name


class Coat(Clothes):

    @property
    def consumption(self):
        return f'Для пошива пальто нужно: {self.name / 6.5 + 0.5 :.2f} ткани'


class Costume(Clothes):

    @property
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.name + 0.3 :.2f} ткани'


coat = Coat(400.0)
costume = Costume(55)
print(coat.consumption)
print(costume.consumption)
