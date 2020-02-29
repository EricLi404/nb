def fib1(n):
    if n < 2:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    print(fib2(10))
