import math

def numDigits(n):
    if n < 10:
        return 1
    else:
        return 1 + numDigits(n//10)

def isPrime(N):

    if N < 0:
        N *= -1

    if N == 2:
        return True

    elif N == 1 or N % 2 == 0:
        return False

    upper = math.sqrt(N)

    divisor = 3

    while divisor <= upper:
        if N % divisor == 0:
            return False

        divisor += 2

    return True

def getDigits(n,arr = []):

    if n < 0:
        return "N/A"

    elif n == 0:
        arr.append(1)
        return arr

    elif n < 10:
        arr.append(n)
        return arr

    else:
        arr.append(n % 10)
        return getDigits(n // 10, arr)

def rotate(s):
    if s < 10:
        return s

    size = numDigits(s)
    temp = s % 10
    s = s // 10

    return temp * 10 ** (size - 1) + s


max = 1000000
total = 0
arr = []

for i in range(0,max):
    arr.append(False)

for i in range(1, max):

    if isPrime(i):
        if i < 10:
            print(i)
            total += 1
        else:
            size = numDigits(i)

            val = True
            num = i


            for j in range(0,size - 1):

                num = rotate(num)

                if arr[num] and num > i:
                    total += 1

                #print(num)
                elif isPrime(num):
                    arr[num] = True

                else:
                    val = False

            if val:
                #print(i)
                total += 1

print(total)