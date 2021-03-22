import math
from useful_routines import primes, isPrime, numDigits, isPandigital, isPalindrome


def P(n):
    return n * (3*n - 1) // 2

def isPentagonal(n):
    value = (math.sqrt(1 + 24 * n) + 1) // 6

    return P(value) == n



pent = []
pent.append(1)

d = 4
index = 0
value = pent[index]
max = 10000000

#while value < max:
 #   value += d
  #  pent.append(value)
   # d += 3



#for i in range(0,len(pent) - 1):
 #   for j in range(i + 1, len(pent)):
  #      sum = pent[j]
   #     diff = pent[i]

    #    if (sum + diff) % 2 == 0:
     #       first = (sum + diff) // 2
      #      second = (sum - diff) // 2

#            if isPentagonal(first) and isPentagonal(second):
 #               print(first,second,diff,sum)


max = 4000

pent = []

for i in range(0,max + 1):
    pent.append(P(i))
print(pent)

for i in range(1,max - 1):
   # print(i)
    for j in range(i + 1, max):
        diff = pent[i]
        sum = pent[j]

        if (sum - diff) % 2 == 0:
            first = (sum - diff) // 2
            second = (sum + diff) // 2

            if isPentagonal(first) and isPentagonal(second):
                print(first,second)




