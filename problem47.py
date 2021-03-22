import math
from useful_routines import primes, isPrime, numDigits, isPandigital, isPalindrome

max = 1000000
p = primes(max)

def factors(n ,p = primes(100)):

    arr = []

    if n == 1:
        return arr

    else:

        i = 0

        while p[i] <= n:
            while n % p[i] == 0:
                n /= p[i]
                if len(arr) == 0 or len(arr) != 0 and arr[len(arr)-1] != p[i]:
                    arr.append(p[i])

            if n == 1:
                break
            else:
                i += 1

        return arr

s = ''


#for i in range(1, max):

#    s+= str(len(factors(i,p)))

print(s)

#for i in range(0, len(s) - 4):
 #   if s[i] == s[i + 1] == s[i + 2] == s[i + 3] == '4':
  #      print(i)

134042

print(len(factors(134043, p)))