from typing import TypeVar, Generic, List
T = TypeVar('T')
h = 0

class Stack(Generic[T]):
    def __init__(self):
        self._container: List[T] = []

    def push(self, item: T):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __repr__(self) -> str:
        #__repr__ - то, что будет выводится при применении к стеку
        #функции print()
        return repr(self._container)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n:int):
    global h
    if n == 1:
        end.push(begin.pop())
        h += 1
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)
        h += 3

def print_towers(): #Облегчает наблюдение за работой основной функции
    print (tower_a)
    print (tower_b)
    print (tower_c)


#Данный алгоритм работает с любым числом дисков.
#Рекомендованное число дисков - до 26.
num_discs = 10

tower_a = Stack()
tower_b = Stack()
tower_c = Stack()

for i in range(1, num_discs + 1):
    tower_a.push(i)

if __name__ == '__main__':
    print("До премещения:")
    print_towers()
    print("-" * 25)
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print("После перемещения:")
    print_towers()
    print("Функция была вызвана ", h, " раз(а).")
