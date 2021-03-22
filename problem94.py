import numpy as np
import math
import itertools
from useful_routines import*

total = 0
max = 333333333


n = 3

while n <= max:

    if n%10000001 ==0:
        print(n)

    val_1 = (3*n-1)*(n+1)
    val_2 = (3*n+1)*(n-1)

    if n%4 == 1:

        if isSquare(val_1):
            total += 3*n-1

        if isSquare(val_2) and val_2%4 == 0:
            total += 3*n+1


    elif n%4 == 3:

        if isSquare(val_2):
            total += 3*n+1

        if isSquare(val_1) and val_1%4 == 0:
            total += 3*n-1

    n += 2



print(total)
