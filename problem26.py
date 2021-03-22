import math

max_cycle = 0
target = 0

numerator = 1

min = 27
max = min + 1

for i in range(min,max):
    remainders = []
    current_rem = 1
    remainders.append(current_rem)
    current_cycle = 0
    numerator = 1

    while current_rem != 0:
        numerator *= 10
        current_rem = numerator % i

        #print(numerator)
        #print(current_rem)

        numerator = current_rem
        #current_digit = numerator // i

        l = len(remainders)
        for j in range(0,l):
            if remainders[j] == current_rem:
                current_cycle = l - j
                break

        if current_cycle != 0:
            break

        remainders.append(current_rem)
        #print(remainders)

    if max_cycle < current_cycle:
        max_cycle = current_cycle
        target = i



print(max_cycle)
print(target)
