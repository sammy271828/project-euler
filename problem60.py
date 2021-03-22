import math
from useful_routines import isTriangle, primes, isPrime

p = primes(100000)

print(p[1],p[3],p[28],p[121])

arr = [1,3,28,121]
values = []

for i in arr:
    values.append(str(p[i]))

print(values)

ans = 0

for i in range(122, len(p)):
    #print(p[i])
    numbers = []
    switch = True
    for j in values:
        numbers.append(str(p[i]) + j)
        if not isPrime(int(numbers[len(numbers) - 1])):
            switch = False
        numbers.append(j + str(p[i]))
        if not isPrime(int(numbers[len(numbers) - 1])):
            switch = False

    if switch:
        print(numbers)
        ans = numbers

print(ans)