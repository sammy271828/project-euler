import math

def divisorCount(n):
    max = math.sqrt(n)
    max2 = math.floor(max)
    total = 0

    for i in range(1,max2):
        if n % i == 0:
            total += 2

    if max % 1 == 0:
        total += 1

    return total

n = 1
val = 1

#while divisorCount(val) <= 500:
 #   n += 1
  #  val = n*(n+1)//2

print(val)