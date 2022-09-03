#Итеративное решение:
def fib3(n):
    n = n - 1
    if n == 0:
        return n #специальный случай
    last = int(0)
    next = int(1)
    for i in range(1, n):
        last, next = next, last + next
    return next


if __name__ == '__main__':
    print ("expectation 7778742049")
    print(fib3(50))
    print ("expectation 4181")
    print (fib3(20))
