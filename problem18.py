import math

f = open('triangle67.txt')
content = f.read()

numbers = []

length_of_string = len(content)

i = 0
while i < length_of_string:
    current_entry = int(content[i] + content[i + 1])
    numbers.append(current_entry)
    i += 3

print(numbers[1])

#numbers = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1, 23, 75, 3, 34, 88, 2, 77, 73, 7, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

rows = 100


for i in range(0,rows-1):
    current_row = rows - i
    start_of_row = current_row * (current_row -1) // 2
    end_of_row = start_of_row + current_row - 1

    if current_row > 1:
        for j in range(start_of_row + 1, end_of_row+1):
            numbers[j - current_row] += max(numbers[j], numbers[j-1])


print(numbers[0])
