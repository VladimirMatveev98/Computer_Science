import re

class Matrix(object):
    """Реализовать разложение по строке и по столбцу(???)"""


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


    def check_integrity():
        #Ищет пробелы в матрице и заполняет их нулями
        pass


    def calc_single():
        #Вычисляет единичную матрицу на основе mat и возвращает её
        pass

    def multiplication(mat_2):
        #Умножает одну матрицу на другую, возвращает третью матрицу
        #return res
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


#Реализовать "проверку целостности", с заполнением нулями пустых мест.
#Т.е. матрица вида 1:1,1 2:1,2 3:2,2 должна быть дополнена 0:2,1

#Реализовать вычисление единичной матрицы.

#Реализовать вычисление определителя матрицы.
