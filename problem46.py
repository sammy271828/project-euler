import math
from useful_routines import isPrime, isSquare

def isGoldbach(n):
    if isPrime(n) or n % 2 == 0:
        return True

    max = int(math.sqrt(n / 2) // 1)
    val = 0

    for i in range(1, max + 1):
        if isPrime(n - 2 * i ** 2):
            return True

    return False

