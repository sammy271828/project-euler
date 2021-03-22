import math

max = 10000

perim = []
perim.append(0)

for i in range(0,max):
    perim.append(0)

upper = 5000

for n in range(1,upper):
    for m in range(n + 1, upper + 1):
        if math.gcd(m,n) == 1:
            print(m,n)
            temp = 2 * m * (m + n)
            current_perim = temp
            while current_perim < len(perim):
                perim[current_perim] += 1
                current_perim += temp

print(perim)

value = 0

print(sum(perim))
for i in range(0,len(perim)):
    if value < perim[i]:
        value = perim[i]
        print(i,value)

print(value)