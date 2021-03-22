import math


def part(total, max):
    coins = [1,2,5,10,20,50,100,200]

    if total == 0:
        return 1

    N = coins[max]

    if N > total:
        #print("hi")
        return part(total,max-1)

    elif max == 0 or N == total:
        return 1

    D = total // N

    value = 0

    for i in range(0,D):
        total -= N

        if total == 0:
            value += 1
            break

        for j in range(0,max):
            value += part(total, j)

   # print(value)
    return value



def partitions(total):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    result = 0

    size = len(coins)

    i = 0

    while coins[i] <= total:
        result += part(total, i)
        i += 1
        print(result)

    return result


value = partitions(200)

print(value)