import math

def fib(N):
    n1 = 1
    n2 = 1
    m = 0

    if N == 1 or N == 2:
        return 1
    else:

        for i in range(0, N-2):
            m = n2
            n2 = n1 + n2
            n1 = m

    return n2

def fib2(N):
    if N == 1 or N == 2:
        return 1
    else:
        return fib2(N-1) + fib2(N-2)

def digits(N):
    return math.floor(math.log10(N) + 1)

m = 4782

print(fib(100))