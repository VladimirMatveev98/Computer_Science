import re

#Добавить UI?
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


    def imp(self,mat_imp):
        #Сокращение от import. ПЕРЕИМЕНОВАТЬ!
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
        #ПЕРЕДЕЛАТЬ. РЕАЛИЗОВАТЬ КАК __str__
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


#-------------------Окончание клааса 'Матрица'---------------------------------
#Реализовать умножение матриц ЧЕРЕЗ ОТДЕЛЬНУЮ ФУНКИЮ.
def matrix_multip(m1,m2):
    #m1 и m2 должны быть объектами класса Matrix
    m_res = Matrix()
    x_1 = 1
    y_1 = 1
    x_2 = 1
    y_2 = 1
    x_res = 1
    y_res = 1
    #Вычисление всей матрицы, проход по строкам m1
    while ???:
        pass
        #Вычисление строки матрицы, проход по столбцам m2
        while ???:
            pass
            #Вычисление одного элемента матрицы:
            while ???:
                pass

    return m_res

#Реализовать вычисление единичной матрицы. ЧЕРЕЗ ОТДЕЛЬНУЮ ФУНКИЮ.

#Реализовать вычисление определителя матрицы. ЧЕРЕЗ ОТДЕЛЬНУЮ ФУНКИЮ.


"""Превратить изначальную задумку в универсальную библиотеку???
Дополнить функционал?"""

#----------------IN PROGRESS------EXPERIMENTAL---------------------------------

if __name__ == '__main__':

    m1 = Matrix()
    #m2 = Matrix()
    m3 = Matrix()


    test_1 = {(1,1):1,(2,1):1,(3,1):1,(1,2):2,(2,2):2,(3,2):2,
            (1,3):3,(2,3):3,(3,3):3}

    test_3 = {(1,1):1,(2,1):2,(3,1):1,(1,2):3,(2,2):4,(3,2):6,
            (1,3):7,(2,3):8,(3,3):9}

    #ИСПРАВИТЬ ПОСЛЕ ПЕРЕИМЕНОВАНИЯ МЕТОДА!!!
    m3.imp(test_3)
    m1.imp(test_1)
    #print('Первый элемент матрицы m3: ', m3.give(1,1))
    m1.print()
    m3.print()
