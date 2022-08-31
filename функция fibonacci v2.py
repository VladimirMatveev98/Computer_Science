memo = {0:0, 1:1} #базовые случаи
n_not_change = True

def fib2(n: int) -> int:
    global n_not_change
    if n_not_change:
        n = n - 1
        n_not_change = False

    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2) #мемоизация
    return memo[n]



if __name__ == '__main__':
    print ("expectation 3")
    print(fib2(5))
    n_not_change = True
    print ("expectation 7778742049")
    print(fib2(50))
