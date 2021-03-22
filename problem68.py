import numpy as np
import math
import itertools
from useful_routines import *


def check_triples(triples):
    total = triples[0][0] + triples[0][1] + triples[0][2]
    for arr in triples:
        if arr[0] + arr[1] + arr[2] != total:
            return False

    return True




lists = list(itertools.permutations([1,2,3,4,5]))
print(lists)

outer = [10,9,8,7,6]



print(outer)


for l in lists:
    triples = []
    inner = l
    for i in range(0,5):
        triples.append([outer[i],inner[i], inner[(i+1)%5]])

    if check_triples((triples)):
        print(triples)
        print(check_triples(triples))




