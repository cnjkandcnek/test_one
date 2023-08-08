import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d
        


def random_class_two(random_class_i):
    ''' Функция рандомизирует координаты и выбор класса '''
    a, b, c, d = [random.randint(0, 100) for i in range(4)]

    if random_class_i == 0:
        return Line(a, b, c, d)
    elif random_class_i == 1:
        return Rect(a, b, c, d)
    else:
        return Ellipse(a, b, c, d)


# создание списка
elements = [random_class_two(random.randint(0,2)) for i in range(217)]


# обнудение координат
for i in elements:
    if isinstance(Line, i):
        i.sp = (0, 0)
        i.ep = (0, 0)


####### Это не нужный комментарий
####### Это не нужный комментарий 2