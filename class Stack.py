class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self,content):
        #Добавляет элемент в стек
        self.stack.append(content)

    def give(self):
        #Возвращает элемент из стека
        if len(self.stack) > 0:
            content = self.stack.pop()
            return content
        else:
            print("Попытка получить значение из пустого стека")
            return False
