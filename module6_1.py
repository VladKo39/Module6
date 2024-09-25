'''
Цель: применить базовые знания о наследовании классов для решения задачи

Задача "Съедобное, несъедобное":
Файл module_6_1.py и загрузите его на ваш GitHub репозиторий и пришлите ссылку на него.
'''

class Animal:
    # класс Animal
    # атрибуты:
    # alive = True(живой)
    #  fed = False(накормленный)
    #  name - индивидуальное название каждого животного.
    alive = True
    fed = False

    def ___init__(self, name: str):
        self.name = name

    def eat(self,food):
        # eat(self,name,food)- метод, где
        #self -параметр класса Animal, название животного
        #food - это параметр, принимающий объекты классов растений.
        self.food = food
        #если food.edible=True(Съедобно, фрукт) то животное съело что-то
        # и накормлено self.fed = True осталось в живых
        #Иначе животное не стало есть что-то и голодно, не живой
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    # класс Plant
    # атрибут:
    # edible = False по умолчанию (съедобность),
    # name - индивидуальное название каждого растения
    edible = False

    def ___init__(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name):
        self.name = name


class Predator(Animal):
    def __init__(self, name):
        self.name = name

class Flower(Plant):
    def __init__(self, name):
        self.name = name
        return
class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True
        return

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)