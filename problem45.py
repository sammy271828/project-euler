import math
from useful_routines import isTriangle, isPentagonal, isHexagonal

i = 144

while i > 0:
    H = i * (2 * i - 1)
    if isPentagonal(H):
        print(H)
        i = 0

    else:
        i += 1

