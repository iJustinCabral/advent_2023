# Day 2 - Snow Day
import re

games_played = []
with open('input.txt', 'r') as file:
    games_played = [games_played.strip() for games_played in file.readlines()]

test_game = games_played[4]
rgb = (0,0,0)
redMax   = 12
greenMax = 13
blueMax  = 14
isPlayable = True
playable_games = []

for game in games_played: 
    game_string = game.split(":", 1)[0]
    game_id = re.search(r'\d+', game_string).group()
    
    print(f'Game ID: {game_id}')

    sets = game.split(":", 1)[1].strip()
    sets = sets.split(";")
    sets = [s.strip() for s in sets]
    
    print(sets)

    for s in sets:
        pairs = s.split(", ")
        isPlayable = True
        
        for pair in pairs:
            rgb = (0, 0, 0)
            value, color = pair.split(" ")
            
            if   color == "red":
                rgb = (value, rgb[1], rgb[2]) 
            elif color == "green":
                rgb = (rgb[0], value, rgb[2]) 
            elif color == "blue":
                rgb = (rgb[0], rgb[1], value) 

            print(rgb)
        
            if int(rgb[0]) > redMax or int(rgb[1]) > greenMax or int(rgb[2]) > blueMax:
                isPlayable = False
                print(isPlayable)
                break
            
        if isPlayable == False:
            break
               
    if isPlayable and game_id not in playable_games:
        playable_games.append(game_id)
        print(playable_games)

int_playable_games = list(map(int, playable_games))

final_sum = sum(int_playable_games)
print(f'The final sum ={final_sum}')
