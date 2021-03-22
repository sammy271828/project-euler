import math

from itertools import permutations
l = list(permutations(range(1, 10)))
print(l[0])

total = 0

for i in l:
    a = 10 * i[0] + i[1]
    b = 100 * i[2] + 10 * i[3] + i[4]
    c = 1000 * i[5] + 100 * i[6] + 10 * i[7] + i[8]

    if a * b == c:
        print(a,b,c)
        total += c

for i in l:
    a = i[0]
    b = 1000 * i[1] + 100 * i[2] + 10 * i[3] + i[4]
    c = 1000 * i[5] + 100 * i[6] + 10 * i[7] + i[8]

    if a * b == c:
        print(a,b,c)
        total += c

total -= 5346 + 5796
print(total)

