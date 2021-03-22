import math
from useful_routines import primes, isPrime, numDigits, isPandigital

p = primes(100000)

size = len(p)


for i in range(0,size):
    if isPandigital(p[i]):
        print(i, p[i])

print(isPrime(7652413))
