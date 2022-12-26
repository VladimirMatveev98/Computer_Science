import re

class Matrix(object):

    def __init__(self):
        self.mat = {}


    def __str__(self):
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

        string = string + '\n'
        return string


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


    def insert(self,mat_imp):
        #Принимает словарь вида {a = x,y} и записывает в матрицу
        self.mat = mat_imp


    def give(self,x,y):
        #Возвращает значение по адресу в матрице
        key = x,y
        return int(self.mat[key])


    def write(self,x,y,cont):
        """Записывает в матрицу элемент на основе принятых X и Y,
        с возможностью перезаписи элемента"""
        self.mat[x,y] = cont


    def last_key(self):
        #Возвращает размерность матрицы
        keys = self.mat.keys()
        keys = list(keys)
        return keys[-1]


    def check(self):
        #Проверяет, есть ли пробелы в матрице
        keys = self.mat.keys()
        keys = list(keys)
        x,y = keys[-1]
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


    def check_integrity(self):
        #Ищет пробелы в матрице и заполняет их нулями
        pass


    def mult_number(number):
        #Умножает матрицу на число
        #Для этого необходимо умножить на число каждый элемент матрицы
        pass

#-------------------Окончание клааса 'Матрица'---------------------------------
#Реализовать умножение матриц ЧЕРЕЗ ОТДЕЛЬНУЮ ФУНКИЮ.

"""Что можно делать с матрицами?
-Сложение матриц;
-Умножение матрицы на число (Метод mult класса Matrix);
-Транспонирование матриц;
-Умножение матриц (def matrix_multip);
-Обратная матрица;
-Вычислить определитель матрицы (def matrix_determinant)"""

def matrix_multip(m1,m2):
    #m1 и m2 должны быть объектами класса Matrix
    #ПРОВЕРИТЬ С ДРУГИМИ МАТРИЦАМИ! БЕЗ ЕДИНИЦ!
    m_res = Matrix()
    c = 0
    x_1 = 1
    y_1 = 1
    x_2 = 1
    y_2 = 1
    x_res = 1
    y_res = 1
    x_max, y_max = m1.last_key()

    while y_1 <= y_max:
        #Вычисление строки матрицы:
        while x_2 <= x_max:
            #Вычисление одного элемента матрицы:
            while x_1 <= x_max:
                a = m1.give(x_1,y_1)
                b = m2.give(x_2,y_2)
                c = c + (a * b)
                x_1 += 1
                y_2 += 1

            m_res.write(x_res,y_res,c)
            x_1 = 1
            y_2 = 1
            c = 0
            x_res += 1
            x_2 += 1

        y_res += 1
        x_res = 1
        x_2 = 1
        y_1 += 1

    return m_res


def matrix_determinant(m1):
    #Вычисляет определитель матрицы
    pass

#Реализовать вычисление единичной матрицы. ЧЕРЕЗ ОТДЕЛЬНУЮ ФУНКИЮ???
"""Превратить изначальную задумку в универсальную библиотеку???
Дополнить функционал?"""

#----------------IN PROGRESS------EXPERIMENTAL---------------------------------

if __name__ == '__main__':

    m1 = Matrix()
    m2 = Matrix()

    test_1 = {(1,1):1,(2,1):1,(3,1):1,(1,2):2,(2,2):2,(3,2):2,
            (1,3):3,(2,3):3,(3,3):3}

    test_2 = {(1,1):1,(2,1):2,(3,1):1,(1,2):3,(2,2):4,(3,2):6,
            (1,3):7,(2,3):8,(3,3):9}

    m1.insert(test_1)
    m2.insert(test_2)

    print(m1)
    print(m2)

    print("РЕЗУЛЬТАТ УМНОЖЕНИЯ ДАННЫХ МАТРИЦ:",'\n' * 2)
    print(matrix_multip(m1,m2))

