# Challenge 2 - Spelled out with letters
import re

# Define a mapping of strings to digits
digit_map = {'one': '1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

lines = []
digits = []
pairs = []
sum = 0

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

print(lines[:10])

def replace_words(s, dm):
    for word, digit in dm.items():
        pattern = r'\W*{}\W*'.format(word)
        s = re.sub(pattern, digit, s)

    return s 

for line in lines:
    line = replace_words(line, digit_map)
    nums = re.findall(r'\d', line)
    line = ''.join(nums)
    
    if len(line) == 0:
        digits.append(int(line[0]) * 11)
    else:
        s = line[0] + line[len(line) - 1]
        digits.append(int(s)) 

print(digits[:10])
for digit in digits:
    sum += digit

print(sum)

