# Challenge 1 - Calibrate Values

# Import the input.txt
lines = []
numbers = []
with open('input.txt', 'r') as file:
    lines = file.readlines()

sum = 0
for line in lines:
    num = [int(char) for char in line if char.isdigit()]
    numbers.append(num)

print(f'number count: {len(numbers)}')
print(f'line count: {len(lines)}')

for number in numbers:
    if len(number) == 1:
        sum += number[0] * 11
    else:
        sum += int(str(number[0]) + str(number[len(number) - 1])) 
print(sum)
