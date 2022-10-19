import re

class Matrix(object):
    global mat
    mat = {}


    def print(self):
        """Доработать вывод, выводить матрицу в виде квадрата в консоль
        соответственно с координатами элементов"""
        print (mat)


    def write_in(self,content,y_now):
        """Принимать строку, разбивать на элементы и записывать как
        первую строку матрицы. Далее принимать вторую строку, записывать
        как вторую строку матрицы. В случае несовпадения длинны строк
        заполнять нулями пустые позиции более коротких строк"""

        x = 1
        y = y_now
        i = 0

        list = re.split(r' ', content)
        x_max = len(list)
        x_max = x_max + 1

        while x < x_max:
            mat [x,y] = list[i]
            x = x + 1
            i = i + 1



m1 = Matrix()
con = ()
y = 1

#Заполнение матрицы:
while con != "qqq":
    con = input(">> ")
    if con == "qqq":
        break
    else:
        m1.write_in(con,y)
        y = y + 1

m1.print()
