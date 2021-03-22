import math

from useful_routines import primes, isPrime

max = 10000
p = primes(max)
size = len(p)
total = 0
upper = 0
counter = 0

for start in range(0, 1000):
    total = 0
    counter = 0
    for i in range(start, size):

        total += p[i]
        counter += 1
        if total > 1000000:
            break

        elif isPrime(total) and counter > upper:
            upper = counter
            print(p[start],counter,total)