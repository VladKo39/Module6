''''''
'''
"Доступ к свойствам родителя. Переопределение свойств."
Цели: Применить сокрытие атрибутов и повторить наследование. Рассмотреть на примере объекта из реального мира.

Пункты задачи:
Создайте классы Vehicle и Sedan.
Напишите соответствующие свойства в обоих классах.
Не забудьте сделать Sedan наследником класса Vehicle.
Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle.

Пример результата выполнения программы:

Исходный код:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

Вывод на консоль:
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: blue
Владелец: Fedos
Нельзя сменить цвет на Pink
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: BLACK
Владелец: Vasyok
Файл с кодом (module_6_2.py) загрузите в репозиторий GitHub и пришлите ссылку на него.
'''


class Vehicle:
    # Родительский класс Vehicle
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    # Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания.

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        # Метод __init__ - инициализация объекта
        self.owner = owner
        # Владелец транспорта. (владелец может меняться)
        self.__model = model
        # Модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = engine_power
        # Мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = color
        # Название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model(self):
        #Метод - возвращает строку: "Модель: <название модели транспорта>"
        return (f'Модель:{" " * 13}{self.__model}')

    def get_horsepower(self):
        #Метод-возвращает строку: "Мощность двигателя: <мощность>"
        return (f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        #Метод - возвращает строку: "Цвет: <цвет транспорта>"
        return f'Цвет:{" " * 15}{self.__color}'

    def print_info(self):
        #Метод - распечатывает результаты методов (в том же порядке):
        print(self.get_model(),
              self.get_horsepower(),
              self.get_color(),
              f'Владелец:{" "*10} {self.owner}',
              sep='\n',end='\n\n')

    def set_color(self, new_color: str):
        #Метод - принимает аргумент new_color(str), меняет цвет __color на new_color,
        #если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись:
        # "Нельзя сменить цвет на <новый цвет>"
        if new_color.lower() in self.__COLOR_VARIANTS:
            __color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}',end='\n\n')


class Sedan(Vehicle):

        __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
print(f'{"*"*10} Первичные свойства {"*"*10}',end="\n\n")
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
print(f'{"*"*10} Смена свойств {"*"*15}',end="\n\n")
vehicle1.print_info()
