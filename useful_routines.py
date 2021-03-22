import math


def relPrime(a,b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1

    if a == 0 or b == 0:
        return False

    elif a == 1 or b == 1:
        return True

    else:
        c = max(a,b)
        d = min(a,b)

        q = c // d

        c -= q * d

        return relPrime(c,d)


def isPalindrome(n):
    s = str(n)
    length = len(s)

    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1

    return True


def isPandigital(n):
    s = str(n)
    if n < 0:
        return isPandigital(-n)

    elif len(s) == 1:
        if n == 1:
            return True
        else:
            return False

    else:
        values = []

        for i in range(0, len(s)):
            values.append(s[i])

        values.sort()

        if values[0] != '1':
            return False
        else:
            counter = 0
            while counter < len(s) and values[counter]  == str(counter + 1):
                counter += 1

            if counter == len(s):
                return True
            else:
                return False


def primes(N):
    primes = []
    numbers = []

    if N < 2:
        return primes

    for i in range(0, N+1):
        numbers.append(True)

    primes.append(2)
    counter = 0
    last = False

    while not last:
        p = 2 * primes[counter]
        while p <= N:
            numbers[p] = False
            p += primes[counter]

        p = primes[counter] + 1

        #find the next prime
        while (not numbers[p]) and p < N:
            p += 1

        if p < N:
            primes.append(p)
            counter += 1
        else:
            last = True

    return primes


def isPrime(N):

    if N < 0:
        N *= -1

    if N == 2:
        return True

    if N == 1 or N % 2 == 0:
        return False

    upper = math.sqrt(N)

    divisor = 3

    while divisor <= upper:
        if N % divisor == 0:
            return False

        divisor += 2

    return True


def numDigits(n):
    if n < 10:
        return 1
    else:
        return 1 + numDigits(n//10)


def isSquare(n):
    if n < 0:
        return False

    m = math.sqrt(n) // 1

    return m ** 2 == n


def isTriangle(n):
    value = (math.sqrt(1 + 8 * n) - 1) // 2

    return value * (value + 1) == 2 * n


def isPentagonal(n):
    value = (math.sqrt(1 + 24 * n) + 1) // 6

    return value * (3 * value - 1) == 2 * n

def isHexagonal(n):
    value = (math.sqrt(1 + 8 * n) + 1) // 4

    return value * (2 * value - 1) == n
