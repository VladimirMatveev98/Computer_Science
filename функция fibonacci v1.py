n_not_change = True

def fib(n: int) -> int:
    """Возвращает n-нное число фибоначи"""
    global n_not_change
    if n_not_change:
        n = n - 1
        n_not_change = False

    if n < 2: #Базовый случай
        return n
    #Рекурсивный случай:
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print ("expectation 144")
    print (fib(13))
    n_not_change = True
    print ("expectation 4181")
    print (fib(20))
