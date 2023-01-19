import re
#Переписать отдельные функции, сделать их частью класса???

class Matrix(object):

    def __init__(self):
        self.mat = {}


    def __str__(self):
        #дополнять пробелами наиболее короткие элементы матрицы?
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


    def __reset__(self):
        #Очищает матрицу.
        self.mat.clear()


    def __check__(self,m1):
        #Проверяет, возможно ли умножение на другую матрицу.
        pass


    def fill(self):
        """Построчно записывает матрицу. Сначала на ввод
        принимается первая строка через пробелы, затем,
        после нажатия ENTER, следующая, до тех пор, пока не введено qqq"""
        y = 1
        content = ()
        print("Начат ввод матрицы с клавиатуры. Вводите значения построчно.")
        print("Между элементами строки ставьте пробел.",
            "Для окончания записи введите qqq.")
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
        print("Матрица записана.")


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


    def mult_number(self,number):
        #Умножает матрицу на число
        m_res = Matrix()
        x_res = 1
        y_res = 1
        x_max, y_max = self.last_key()
        while y_res <= y_max:
            while x_res <= x_max:
                cont = self.give(x_res,y_res)
                m_res.write(x_res,y_res,cont * number)
                x_res += 1

            x_res = 1
            y_res += 1

        return m_res

#-------------------Окончание клааса 'Матрица'---------------------------------

def matrix_multip(m1,m2):
    #m1 и m2 должны быть объектами класса Matrix
    #На данный момент работает корректно только с квадратными матрицами.
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
    x_max, y_max = m1.last_key()
    if x_max == y_max:
        print("Нахождение определителя возможно")

    else:
        print("Матрица не квадратная, нахождение определителя невозможно")
        return False


#----------------IN PROGRESS------EXPERIMENTAL---------------------------------

if __name__ == '__main__':

    m1 = Matrix()
    m2 = Matrix()
    m3 = Matrix()

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

    print("РЕЗУЛЬТАТ УМНОЖЕНИЯ ПЕРВОЙ МАТРИЦЫ НА 2:",'\n' * 2)
    m3 = m1.mult_number(2)
    print(m3)

    #print("ВЫЧИСЛЕНИЕ ОПРЕДЕЛИТЕЛЯ ВТОРОЙ МАТРИЦЫ:",'\n' * 2)
    #print(matrix_determinant(m2))

    """print("УМНОЖЕНИЕ МАТРИЦ, ВВОДИМЫХ С КЛАВИАТУРЫ:",'\n' * 2)
    m4 = Matrix()
    m5 = Matrix()
    m4.fill()
    m5.fill()
    print(matrix_multip(m4,m5))"""

