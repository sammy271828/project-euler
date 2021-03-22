import math

current_list = [1,1]
counter = 0

for i in range(0,99):
    new_list = [1]

    for j in range(0,len(current_list) - 1):
        new_list.append(current_list[j] + current_list[j + 1])
    new_list.append(1)

    #print(new_list)

    for X in new_list:
        if X > 1000000:
            print(X)
            counter += 1

    current_list = new_list

print(counter)