import math
from useful_routines import primes, isPrime, numDigits, isPandigital, isPalindrome

p = primes(10000)


n = max(p)

max = len(p)

min = 0
while p[min] < 1000:
    min += 1

for i in range(min,max-2):
    for j in range(i + 1, max):
        mid = (p[i] + p[j]) // 2

        if isPrime(mid):
            first = str(p[i])
            second = str(mid)
            third = str(p[j])

            if ''.join(sorted(first)) == ''.join(sorted(second)) == ''.join(sorted(third)) :
                print(p[i],mid,p[j])

s = '483823'
t = ''.join(sorted(s))

print(t)