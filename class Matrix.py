import re

class Matrix(object):
    """Реализовать разложение по строке и по столбцу"""


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


    def imp(self,mat_imp):
        #Сокращение от import
        "Принимает словарь вида {a = x,y} и записывает в матрицу"
        self.mat = mat_imp
        print("Импортирование матрицы прошло успешно.")


    def give(self,x,y):
        """Возвращает значение по адресу в матрице"""
        key = x,y
        return int(self.mat[key])


    def check(self):
        #Проверяет, есть ли пробелы в матрице
        keys = self.mat.keys()
        keys = list(keys)
        key = keys[-1]
        x,y = key
        x_check = 1
        y_check = 1
        check_elements = 0
        try:
            while x_check <= x:
                while y_check <= y:
                    check_elements += 1
                    y_check = y_check + 1
                x_check = x_check + 1
                y_check = 1
            return True
        except:
            return False

    def write(self,x,y,cont):
        """Записывает в матрицу элемент на основе принятых X и Y,
        с возможностью перезаписи элемента"""
        self.mat[x,y] = cont


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
                string = string + '|' + str(self.mat[x,y])
                x = x + 1
            string = string + '|' + '\n'
            x = 1
            y = y + 1

        print ('\n')
        print (string)


    def check_integrity(self):
        #Ищет пробелы в матрице и заполняет их нулями
        pass


    def calc_single(self):
        #Вычисляет единичную матрицу на основе mat и возвращает её
        pass


    def mult(self,mat_2):
        mat_1 = self.mat
        mat_2 = mat_2
        res = Matrix()
        print("Вызван метод умножения")
        #Проводим проерку размерности:
        keys = self.mat.keys()
        keys = list(keys)
        keys_1 = keys[-1]
        keys_2 = mat_2.last_key()
        print (keys_1, keys_2)
        if keys_1[1] == keys_2[0]:
            print("Умножение возможно!")
            check = True
        else:
            print("Умножение невозможно.")
            print("Матрицы несогласованы.")
            check = False
            res = False

        if check:
            print("Продолжим....")
            x_max,y_max = keys_1
            x = 1
            y = 1
            while x <= x_max:
                a = mat_1.give(x,y)
                b = mat_2.give(y,x)
                x += 1
                y += 1

        #Умножает одну матрицу на другую, возвращает третью матрицу
        return res




#Реализовать умножение матриц. Пусть матрица имеет метод умножение,
#Принимающий в качестве аргумента другую матрицу и возвращающий
#матрицу-результат.

#Реализовать вычисление единичной матрицы.

#Реализовать вычисление определителя матрицы.


"""Реализовать методы работы с матрицами через функции вне класса???
Превратить изначальную задумку в универсальную библиотеку???
Дополнить функционал?"""

#----------------IN PROGRESS------EXPERIMENTAL---------------------------------

if __name__ == '__main__':

    m1 = Matrix()
    #m2 = Matrix()
    m3 = Matrix()

    #Заполнение матрицы:
    #m1.fill()
    #m3.fill()
    #Вывод на печать:
    #m1.print()
    #Возврат перового элемента матрицы:
    #print('Первый элемент матрицы m1: ', m1.give(1,1))

    test_1 = {(1,1):1,(2,1):1,(3,1):1,(1,2):2,(2,2):2,(3,2):2,
            (1,3):3,(2,3):3,(3,3):3}

    test_3 = {(1,1):1,(2,1):2,(3,1):1,(1,2):3,(2,2):4,(3,2):6,
            (1,3):7,(2,3):8,(3,3):9}

    m3.imp(test_3)
    m1.imp(test_1)
    #print('Первый элемент матрицы m3: ', m3.give(1,1))
    m1.print()
    m3.print()

    m4 = m3.mult(m1)
