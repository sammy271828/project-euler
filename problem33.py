import math

def isCancellative(m,n):
    if m >= n or n >= 100 or m < 10 or n % 10 == 0 or m % 10 == 0:
        return False
    else:
        a = m // 10
        b = m % 10

        c = n // 10
        d = n % 10


        if (a == c and m * d == n * b) or (a == d and m * c == n * b) or (b == c and m * d == n * a) or (b == d and m * c == n * a):
            print(a, b, c, d)
            return True

        else:
            return False



for i in range(10,100):
    for j in range(1,i):
        isCancellative(j,i)

print(16*26*19*49, 64*65*95*98)