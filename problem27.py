import math

n = math.sqrt(2)


def isPrime(N):

    if N < 0:
        N *= -1

    if N == 2:
        return True

    if N == 1 or N % 2 == 0:
        return False

    upper = math.sqrt(N)

    divisor = 3

    while divisor < upper:
        if N % divisor == 0:
            return False

        divisor += 2

    return True

primes = []

n = 2
while n < 1000:
    if(isPrime(n)):
        primes.append(n)
    n += 1

print(primes)
print(1/997)

A = 1
B = 41
product = 41
no_of_primes = 40

for a in range(-999, 1000):
    for b in range(-177,178):
        n = 0
        current_primes = 0
        if b < 0:
            b = - primes[-b]
        else:
            b = primes[b]

        while isPrime(n**2 + a*n + b):
            current_primes += 1
            n += 1

        if current_primes > no_of_primes:
            no_of_primes = current_primes
            product = a * b
            A = a
            B = b

