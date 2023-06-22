class Matrix:
    def __init__(self):
        self.mat = []


    def __str__(self):
        string = ''
        for i in self.mat:
            for j in i:
                string += str(j) + " "
            string += '\n'
        return string


    def insert(self,list):
        self.mat = list




if __name__ == '__main__':

    test_1 = [[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5]]

    test_2 = [[9, 8, 7],
              [8, 7, 6],
              [7, 6, 5]]

    m1 = Matrix()
    m2 = Matrix()

    m1.insert(test_1)
    m2.insert(test_2)

    print(m1)
    print(m2)
