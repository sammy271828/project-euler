import math
from useful_routines import primes, isPrime, numDigits, isPandigital, isPalindrome

sum = 0

for i in range(1, 1000000):
    if isPalindrome(i) and isPalindrome('{0:b}'.format(i)):
        print(i, '{0:b}'.format(i))
        sum += i

print(sum)

