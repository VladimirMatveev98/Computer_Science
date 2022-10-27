import re

class Matrix(object):


    def __init__(self):
        self.mat = {}


    def fill(self):
        """Построчно записывает матрицу. Сначала на ввод
        принимается первая строка через пробелы, затем,
        после нажатия ENTER, следующая, до тех пор, пока не введено qqq"""

        x = 1
        y = 1
        i = 0
        content = ()

        while content != "qqq":
            x = 1
            content = input(">> ")
            if content == "qqq":
                break
            else:
                list = re.split(r' ', content)
                x_max = len(list)
                x_max = x_max + 1

            i = 0
            while x < x_max:
                self.mat [x,y] = list[i]
                x = x + 1
                i = i + 1

            y = y + 1


    def give(self,x,y):
        """Возвращает значение по адресу в матрице"""
        key = x,y
        return int(self.mat[key])


    def write(self,cont,x,y):
        """Записывает в матрицу элемент на основе принятых X и Y,
        с возможностью перезаписи элемента"""
        pass


    def last_key(self):
        keys = self.mat.keys()
        keys = list(keys)
        return keys[-1]


    def print(self):
        """Выводит в консоль матрицу в соответствии с
        координатами её элементов"""
        keys = self.mat.keys()
        keys = list(keys)
        max_x, max_y = keys[-1]
        x = 1
        y = 1
        string = str()
        while y < max_y + 1:
            while x < max_x + 1:
                string = string + '|' + self.mat[x,y]
                x = x + 1
            string = string + '|' + '\n'
            x = 1
            y = y + 1

        print ('\n')
        print (string)


    def calc_single():
        #Вычисляет единичную матрицу на основе mat и возвращает её
        pass


m1 = Matrix()
m2 = Matrix()

#Заполнение матрицы:
m1.fill()
#Вывод на печать:
m1.print()
#Возврат перового элемента матрицы:
print('Первый элемент матрицы m1: ', m1.give(1,1))


m2.fill()

m1.print()
m2.print()

#Реализовать умножение матриц. Пусть матрица имеет метод умножение,
#Принимающий в качестве аргумента другую матрицу и возвращающий
#матрицу-результат.

#Реализовать вычисление единичной матрицы.

#Реализовать вычисление определителя матрицы.
