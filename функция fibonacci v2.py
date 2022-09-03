memo = {0:0, 1:1} #базовые случаи

def fib2(a):
    #Уменьшает n для корректного результата
    n = int(a) - 1
    return calc2(n)

def calc2(n):
    #Вычисление с применением мемоизации:
    if n not in memo:
        memo[n] = calc2(n - 1) + calc2(n - 2) #мемоизация
    return memo[n]


if __name__ == '__main__':
    print ("expectation 3")
    print(fib2(5))
    print ("expectation 7778742049")
    print(fib2(50))
