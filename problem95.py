import numpy as np
import math
import itertools
from useful_routines import *


def divisor_sum(N):

    if N < 4:
        return 1

    bound = math.floor(math.sqrt(N))
    sum = 1

    if bound**2 == N:
        sum += bound

    else:
        for i in range(2,bound + 1):
            if N % i == 0:
                sum += i + N//i




    return sum


print(divisor_sum(276))

max = 1000
chains = []
values = []

for i in range(0,max):
    chains.append([])

#print(chains)

chains[2].append(1)

values = [6, 28, 220, 496, 1184, 2620, 5020, 6232, 8128, 10744, 12285, 12496, 14316, 17296, 63020, 66928, 67095, 69615, 79750, 100485, 122265, 122368, 141664, 142310, 171856, 176272, 185368, 196724, 280540, 308620, 319550, 356408, 437456, 469028, 503056, 522405, 600392, 609928, 624184, 635624, 643336, 667964, 726104, 802725, 879712, 898216]
total = 0

for x in values:
    count = 0
    val = divisor_sum(x)
    current_chain = [x,val]
    count+=1

    while val != x:
        val = divisor_sum(val)
        current_chain.append(val)
        count+=1

    if count > total:
        total = count

    print(current_chain)


for i in range(3,max):
    val = divisor_sum(i)

    if i%1000 == 0:
        print(i)


    while i < val < max and val not in chains[i]:
        chains[i].append(val)
        val = divisor_sum(val)
        #print(val)

    if val==i:
        values.append(i)

#print(chains)
print(values)

#print(chains)
#chains = []

#values = []

'''
for i in range(2,max+1):
    length = 1

    current_chain = []

    val = i
    print(val)
    while val > 1:
        current_chain.append(val)
       # print(current_chain)
        val = divisor_sum(val)

        if val == i:
            chains.append(i)
            values.append(len(current_chain))
            break

        elif val in chains or val > max or val in current_chain:
            break
'''
