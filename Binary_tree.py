class Tree():
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data


    def print_tree(self):
        print(self.data)
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()


    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data



    def how_numbers_in_range(self,tuple,total = 0):
        self.minimum,self.maximum = tuple
        self.res = total
        if self.data >= self.minimum:
            if self.data <= self.maximum:
                self.res = self.res + 1
        if self.left:
            self.res = self.left.how_numbers_in_range(tuple,self.res)
        if self.right:
            self.res = self.right.how_numbers_in_range(tuple,self.res)

        return self.res


def create_binary_tree(tree,list):
    for i in list:
        tree.insert(i)



if __name__ == '__main__':

    list_of_values = [7, 9, 2, 5, 1, 6, 8]

    tree = Tree(list_of_values[0])
    create_binary_tree(tree,list_of_values)
    #tree.print_tree()

    minimum = int(input("Введите минимальное значение для поиска: "))
    maximum = int(input("Введите максимальное значение для поиска: "))
    print("\nРЕЗУЛЬТАТ В ЗАДАННОМ ДИАПАЗОНЕ: ",
            tree.how_numbers_in_range((minimum,maximum)))
