import math
from useful_routines import primes, isPrime, numDigits, isPandigital, isPalindrome

s = '0'
max = 1000000

for i in range(1,max):
    s += str(i)

index = 1
result = int(s[index])


for i in range(0,6):
    index *= 10
    result *= int(s[index])

print(result)