import math
from useful_routines import isPandigital

#upper bound of 9999

for i in range(900,1000):
    s = str(i)
    t = str(i * 2)
    u = str(i * 3)

    n = int(s + t + u)
    if isPandigital(n):
        print(n)

for i in range(9123,10000):
    s = str(i)
    t = str(i * 2)

    n = int(s + t)
    if isPandigital(n):
        print(i, 2*i, n)