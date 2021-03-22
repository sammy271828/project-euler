import numpy as np
import math
import fractions as f
from useful_routines import *


class pair:
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b

    def get_num(self):
        return self.a

    def get_denom(self):
        return self.b

    def recip(self):
        temp = self.a
        self.a = self.b
        self.b = temp

    def reduce(self):
        factor = math.gcd(self.a, self.b)
        self.a /= factor
        self.b /= factor

    def print(self):
        print(self.a, '/', self.b)



def sum(x,y):
    x_a = x.get_num()
    x_b = x.get_denom()

    y_a = y.get_num()
    y_b = y.get_denom()

    num = x_a*y_b + y_a*x_b
    denom = y_b*x_b

    return pair(num, denom)


def iterate(input, depth = 0):
    z = pair(2,1)
    z = sum(z,input)
    z.recip()

    return z

def approx(steps):
    max = steps
    z = pair(1, 2)

    for i in range(0, max):
        z = iterate(z)

    z = sum(pair(1, 1), z)

    return z

total = 0

for i in range(0,1000):
    z = approx(i)
    a = z.get_num()
    b = z.get_denom()

    a_num = numDigits(a)
    b_num = numDigits(b)

    if a_num > b_num:
        total += 1


print(total)