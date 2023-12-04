"""
Advent of Code Day 2: Cube Conundrum - Puzzle 1
Author: Chris Smith
Description: Given a game in which cubes are drawn from a bag with an unknown number of cubes,
    this program will determine which games are possible with the given numbers of 12 red, 13
    green and 14 blue cubes.
"""

#### FUNCTIONS ####

# Function to split game into rounds by semicolons, slicing past the game number
def split_games_into_rounds(game):
    rounds = game[(game.index(':') + 2):].split('; ')
    return rounds

# Function to split rounds into colors
def split_rounds_into_colors(round):
    colors = round.split(', ')
    return colors


#### MAIN CODE ####

# Open the file and place each line in a list
with open('day2_cube_conundrum/puzzle_input2.txt', 'r') as file:
    raw_data = file.read()
    data = raw_data.split('\n')

print(split_games_into_rounds(data[3])[1].split(', '))
