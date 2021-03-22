import math
from useful_routines import isTriangle

import math
from useful_routines import primes, isPrime

max = 101

p = []

for i in range(1, max):
    p.append(i)

table = []
sums = []

table.append(0), sums.append(0)
table.append([1]), sums.append(1)

for i in range(2, max):
#    j = 0
    current = []
    for j in range(0, len(p)):
        val = i - p[j]

        if val <= 0:
            break
        else:
            temp = 0
            size = min(len(table[val]), j + 1)

            if size == len(table[val]):
                current.append(sums[val])
            else:
                for k in range(0, len(table[val])):
                    if k < j + 1:
                        temp += table[val][k]
                    else:
                        break

                current.append(temp)

    if p[j] == i:
        current.append(1)

    table.append(current)
    sums.append(sum(current))
    print(i)

for i in range(2, len(table)):
    print(i, sum(table[i]))

print(table)