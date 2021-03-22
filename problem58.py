import math
from useful_routines import isTriangle, isPrime



ratio = 1
n = 1
primes = []

while ratio > 1/10:
    n += 2
    corner = n ** 2

    for i in range(1,4):
        val = n ** 2 - i * (n-1)
        if isPrime(val):
            primes.append(val)

    ratio = len(primes) / (2 * n - 1)
    print(n,ratio)
