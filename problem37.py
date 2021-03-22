import math
from useful_routines import primes, isPrime, numDigits, isPandigital, isPalindrome

p = primes(1000000)

def isTruncatable(n):

    s = str(n)
    current_left = ''
    current_right = ''

    for i in range(0,len(s)):
        current_left += s[i]
        current_right = s[len(s)-1-i] + current_right

        current_intl = int(current_left)
        current_intr = int(current_right)


        if not isPrime(current_intl) or not isPrime(current_intr):
            return False

    return True

sum = 0
counter = 0

for i in p:
    if i < 10:
        continue
    else:
        if isTruncatable(i):
            print(i)
            sum += i
            counter += 1


print(sum)
print(counter)
