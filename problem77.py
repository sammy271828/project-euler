import math
from useful_routines import primes, isPrime

max = 10000

i = 5
p = primes(max)

table = []
sums = []

table.append(0), sums.append(0)
table.append(0), sums.append(0)
table.append([1]), sums.append(1)
print(table)

for i in range(3, max):
#    j = 0
    current = []

    for j in range(0, len(p)):
        val = i - p[j]

        if val <= 0:
            break
        elif val < 2:
            current.append(0)
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