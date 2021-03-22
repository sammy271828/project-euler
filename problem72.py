import math
from useful_routines import primes, isPrime, numDigits, isPandigital, isPalindrome, relPrime
max = 100000

global p
global total

total = 0
p = primes(max)

def totient(arr):
    i = 0
    current = arr[0]
    val = 0
    counter = 0

    while arr[i] >= 0:
        if arr[i + 1] < arr[i]:
            val += p[arr[i]] ** (counter) * (p[arr[i]] - 1)
            counter = 0
        else:
            counter += 1

        i += 1

    return val



def compute(arr):
    max = len(p)
    val = 1

    for i in arr:
        if 0 <= i < max:
            val *= p[i]

    return val


def increment(arr):
    if len(arr) == 0 or arr[0] < 0:
        arr[0] = 0
    else:
        last = len(arr) - 1
        current = last - 1

        if arr[current] > arr[last]:
            arr[last] += 1
        else:
            while 0 <= current and arr[current] == arr[last]:
                if current > 0 and arr[current] == arr[current - 1]:
                    arr[current] = -1

                current -= 1

            arr[last] = -1

            arr[current + 1] += 1

        while compute(arr) > 1000000:
            first_positive = last

            while arr[first_positive] < 0:
                first_positive -= 1

            if first_positive == 0:
                return
            else:
                while arr[first_positive] == arr[first_positive - 1]:
                    arr[first_positive] = -1
                    first_positive -= 1

                arr[first_positive] += 1



code = []


for i in range(0,20):
    code.append(-1)


#while code[0] < 78498:
 #   increment(code)
  #  print(p[code[0]])
   # total += totient(code)

print(len(p))
print(total)