import re

class Matrix(object):
    global mat
    mat = {}

    def fill(self):
        """Принимать строку, разбивать на элементы и записывать как
        первую строку матрицы. Далее принимать вторую строку, записывать
        как вторую строку матрицы. В случае несовпадения длинны строк
        заполнять нулями пустые позиции более коротких строк"""

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
                mat [x,y] = list[i]
                x = x + 1
                i = i + 1

            y = y + 1

    def give(self,x,y):
        """Возвращает значение по адресу в матрице"""
        key = x,y
        return mat[key]

    def __last_key__(self):
        keys = mat.keys()
        keys = list(keys)
        return keys[-1]


    def print(self):
        """Доработать вывод, выводить матрицу в виде квадрата в консоль
        в соответствии с координатами элементов"""
        #print (mat)
        keys = mat.keys()
        keys = list(keys)
        max_x, max_y = keys[-1]
        #print(max_x, max_y)
        x = 1
        y = 1
        string = str()
        while y < max_y + 1:
            while x < max_x + 1:
                string = string + '|' + mat[x,y]
                x = x + 1
            string = string + '|' + '\n'
            x = 1
            y = y + 1
        print ('\n')
        print (string)


m1 = Matrix()
con = ()

#Заполнение матрицы:
m1.fill()
#Вывод на печать:
m1.print()
#Возврат перового элемента матрицы:
print('Первый элемент матрицы: ', m1.give(1,1))
#m1.last_key()
