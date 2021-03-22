import math
from useful_routines import isPalindrome

total = 0

def reverse(s):
    t = ''
    max = len(s)
    for i in range(1,max+1):
        t += s[max - i]
    return t

def iterate(s):
    a = int(s)
    b = int(reverse(s))
    return str(a + b)


for i in range(1,10001):
    counter = 1
    s = str(i)
    a = iterate(s)

    while not isPalindrome(int(a)) and counter < 50:
        a = iterate(a)
        counter += 1

    if counter < 50:
        print(i, a, counter)
        total += 1


print(10000 - total)
