import math


primes = [2,3,5,7,11,13]

def P(n, sides):
    if sides == 3:
        return n*(n+1)//2
    elif sides == 4:
        return n**2
    elif sides == 5:
        return n*(3*n - 1) // 2
    elif sides == 6:
        return n * (2*n - 1)
    elif sides == 7:
        return n*(5*n - 3) // 2
    elif sides == 8:
        return n * (3*n - 2)

totals = []
numbers = []

for i in range(3,9):
    counter = 0
    n = 10
    arr = []
    while 0 < P(n,i) < 10000:
        if P(n,i) > 999:
            #print(i, P(n,i))

            s = str(P(n,i))
            value = int(s[2] + s[3])
            if value >= 10:
                print(s)
                arr.append(s)
                counter += 1
        n += 1
    totals.append(counter)
    numbers.append(arr)
    print("There are exactly %d elements with four digits", counter)
    print("***********")

print(numbers)
print(totals)
print(sum(totals))

val = 1
for i in range(0,len(totals)):
    val *= totals[i]

print(val)


cycle = []
counter = 0
i = 0

for n in numbers[5]:
    cycle = []
    current_head = n[2] + n[3]
    cycle.append(n)

    if int(current_head) >= 10:
        for m in numbers[0]:
            if m[0] + m[1] == current_head:
               # current_head = m[2] + m[3]
                cycle.append(m)
                print(cycle)
                counter += 1


                #if int(current_head) >= 10:
                 #   for m in numbers[1]:
                  #      if m[0] + m[1] == current_head:
                   #         current_head = m[2] + m[3]
                    #        cycle.append(m)
                     #       print(cycle)
                      #      counter += 1


print(counter)

table = []
entry = []

for i in range(0,100):
    table.append(0)

#for i in range(0,6):
 #   for n in numbers[i]:
  #      val = int(n[0] + n[1])
   #     table[val].append(n)

for i in range(10,100):
    list = []
    for j in range(0,6):
        for n in numbers[j]:
            val = int(n[0] + n[1])
            if val == i:
                local = [j, n]
                list.append(local)
    table[i] = list



for n in numbers[5]:
    current_cycle = []
    counter = 1
    key = primes[5]
    key_values = [5]
    val = int(n[2] + n[3])

    current_cycle.append(n)

    for i in table[val]:
        if key % primes[i[0]] != 0:
            key *= primes[i[0]]
            current_cycle.append(i[1])
            key_values.append(i[0])
            val2 = int(i[1][2] + i[1][3])

            for j in table[val2]:
                if key % primes[j[0]] != 0:
                    key *= primes[j[0]]
                    current_cycle.append(j[1])
                    key_values.append(j[0])
                    val3 = int(j[1][2] + j[1][3])

                    for k in table[val3]:
                        if key % primes[k[0]] != 0:
                            key *= primes[k[0]]
                            current_cycle.append(k[1])
                            key_values.append(k[0])
                            val4 = int(k[1][2] + k[1][3])

                            for l in table[val4]:
                                if key % primes[l[0]] != 0:
                                    key *= primes[l[0]]
                                    current_cycle.append(l[1])
                                    key_values.append(l[0])
                                    val5 = int(l[1][2] + l[1][3])

                                    for m in table[val5]:
                                        if key % primes[m[0]] != 0:
                                            key *= primes[m[0]]
                                            current_cycle.append(m[1])
                                            key_values.append(m[0])
                                            val6 = int(m[1][2] + m[1][3])
                                            first = current_cycle[0]

                                            if val6 == int(first[0] + first[1]):
                                                print(current_cycle)
                                                for p in range(0, len(current_cycle)):
                                                    current_cycle[p] = int(current_cycle[p])
                                                print(sum(current_cycle))


                                            key //= primes[m[0]]
                                            key_values.pop()
                                            current_cycle.pop()


                                    key //= primes[l[0]]
                                    key_values.pop()
                                    current_cycle.pop()

                            key //= primes[k[0]]
                            key_values.pop()
                            current_cycle.pop()

                    key //= primes[j[0]]
                    key_values.pop()
                    current_cycle.pop()

            key //= primes[i[0]]
            key_values.pop()
            current_cycle.pop()




