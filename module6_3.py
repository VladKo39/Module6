''''''
'''
"Множественное наследование"
Задача "Мифическое наследование":
Необходимо написать 3 класса:
Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
Пункты задачи:
Создайте классы родители: Horse и Eagle с методами из описания.
Создайте класс наследник Pegasus с методами из описания.
Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.

Пример результата выполнения программы:
Пример работы программы:
p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()
Вывод на консоль:
(0, 0)
(10, 15)
(5, 35)
I train, eat, sleep, and repeat
Файл module_6_3.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
'''


class Horse:
    # Horse - класс лошадь.
    # Атрибут класса:
    x_distance = 0
    # пройденный путь.
    sound = 'Frrr'
    # звук, который издаёт лошадь.

    def __init__(self):
        # Для наследства
        super().__init__()

    def run(self, dx):
        # Метод класса Horse:
        # где dx - изменение дистанции, увеличивает x_distance на dx.
        self.x_distance += dx


class Eagle:
    # Eagle класс орёл.
    # Атрибут класса:
    y_distance = 0
    # высота полёта
    sound = 'I train, eat, sleep, and repeat'
    # звук, который издаёт орёл (отсылка)

    def __init__(self):
        self.sound = Eagle.sound

    def fly(self, dy):
        # Метод класса Eagle:
        # где dy - изменение дистанции, увеличивает y_distance на dy.
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    # класс Пегас. Наследуется от Horse и Eagle в том же порядке.

    def move(self, dx, dy):
        # move(self) - где dx и dy изменения дистанции.
        # В этом методе должны запускаться
        super().run(dx)
        # наследованный метод run
        super().fly(dy)
        ##наследованный метод fly

    def get_pos(self):
        # Метод класса:
        distance = (self.x_distance, self.y_distance)
        return distance
        # возвращает текущее положение пегаса в виде кортежа (x_distance, y_distance)

    def voice(self):
        # voice - который печатает значение унаследованного атрибута sound.
        super().__init__()
        print(self.sound)


p1 = Pegasus()
print(f'{"*" * 10} Определение объекта класса {type(p1).__name__} {"*" * 10}')
print(f'{"*" * 10} Определение начальной позиции объекта {type(p1).__name__} {"*" * 24}')
print(p1.get_pos())
p1.move(10, 15)
print(f'{"*" * 10} Определение позиции объекта {type(p1).__name__} после первого изменения {"*" * 10}')
print(p1.get_pos())
p1.move(-5, 20)
print(f'{"*" * 10} Определение позиции объекта {type(p1).__name__} после второго изменения {"*" * 10}')
print(p1.get_pos())
print(f'{"*" * 10} Последнее слово {type(p1).__name__} в роли Eagle {"*" * 33}')
p1.voice()
