# Day 3 Challenge - Gear Ratios!!
import re

gear_ratios = []
sc_arr = []

with open('input.txt', 'r') as file:
    gear_ratios = [gear_ratios.strip() for gear_ratios in file.readlines()]


sc_array = list(set([char for string in gear_ratios for char in string if not char.isdigit() and char!= "."]))

def sum_gear_ratios(gears):
    sum = 0
    for i in range(len(gears)):
        for j in range(len(gears[i])):
            if gears[i][j].isdigit():
                for x in range(max(0, i-1), min(len(gears), i+2)):
                    for y in range(max(0, j-1), min(len(gears[i]), j+2)):
                        if (x, y) != (i, j) and gears[x][y] in sc_array:
                            sum += int(gears[i][j])
                            break
                if i > 0 and j > 0 and gears[i-1][j-1] in sc_array:
                    sum += int(gears[i][j])
                if i > 0 and j < len(gears[i])-1 and gears[i-1][j+1] in sc_array:
                    sum += int(gears[i][j])
                if i < len(gears)-1 and j > 0 and gears[i+1][j-1] in sc_array:
                    sum += int(gears[i][j])
                if i < len(gears)-1 and j < len(gears[i])-1 and gears[i+1][j+1] in sc_array:
                    sum += int(gears[i][j])
    return sum



print(sc_array)
print(sum_gear_ratios(gear_ratios))


