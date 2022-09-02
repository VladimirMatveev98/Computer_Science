n_not_change = True
#Итеративное решение:
def fib3(n: int) -> int:
    global n_not_change
    if n_not_change:
        n = n - 1
        n_not_change = False

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
    n_not_change = True
