def fib(a):
    #Уменьшает n для корректного результата
    n = int(a) - 1
    return calc(n)

def calc(n):
    #Вычисляет n+1 по счёту число фибоначчи
    if n < 2: #Базовый случай
        return n
    #Рекурсивный случай:
    return calc(n - 1) + calc(n - 2)


if __name__ == '__main__':
    print ("expectation 144")
    print (fib(13))
    print ("expectation 4181")
    print (fib(20))
