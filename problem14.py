import math

def collatz(n):
    if n == 1:
        return False
    elif n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def chain_length(n):
    current_chain = 1

    while(collatz(n)):
        n = collatz(n)
        current_chain += 1

    return current_chain

max = 1000000
max_chain = 0
max_number = 1

lengths = []

for i in range(0,max+1):
    lengths.append(-1)

lengths[1] = 1

for i in range(2,max+1):
    current_chain = 1

    n = i

    while n != 1:
        n = collatz(n)

        if n <= max and lengths[n] > 0:
            current_chain += lengths[n]
            lengths[i] = current_chain
            n = 1
        else:
            current_chain += 1


for i in range(1,len(lengths)):
    if lengths[i] > max_chain:
        max_chain = lengths[i]
        max_number = i


