# Day 2 - Part 2 (Power Set of Cubes)
import re

games_played = []
with open('input.txt', 'r') as file:
    games_played = [games_played.strip() for games_played in file.readlines()]

test_game = games_played[4]
total_sum = 0

for game in games_played:
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    power_set = 0

    sets = game.split(":", 1)[1].strip()
    sets = sets.split(";")
    sets = [s.strip() for s in sets]

    print(sets)

    for s in sets:
        pairs = s.split(", ")
        tempRed = 0
        tempGreen = 0
        tempBlue = 0
        rgb = (0, 0, 0)
        
        for pair in pairs:
            value, color = pair.split(" ")
            
            if   color == "red":
                rgb = (value, rgb[1], rgb[2]) 
            elif color == "green":
                rgb = (rgb[0], value, rgb[2]) 
            elif color == "blue":
                rgb = (rgb[0], rgb[1], value) 

        print(rgb)

        tempRed = int(rgb[0])
        tempGreen = int(rgb[1])
        tempBlue = int(rgb[2])

        if tempRed >= maxRed:
            maxRed = tempRed
        
        if tempGreen >= maxGreen:
            maxGreen = tempGreen
        
        if tempBlue >= maxBlue:
            maxBlue = tempBlue

        print(f'R:{maxRed} G:{maxGreen} B:{maxBlue}')
        
    power_set = maxRed * maxGreen * maxBlue
    total_sum += power_set

    print(power_set)


print(total_sum)

