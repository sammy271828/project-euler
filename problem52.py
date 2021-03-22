import math
from useful_routines import primes

p = primes(1000001)
print(p)

a = 1546346236

def sort_digits(a):
    s = str(a)
    arr = []

    for i in range(0,len(s)):
        arr.append(int(s[i]))

    arr.sort()

    return arr


max = 10000

for i in range(1,max):
    arr = sort_digits(i)
    val = True
    for j in range(2,7):
        if sort_digits(j * i) != arr:
            val = False
            break
    if val:
        print(i)


