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

# Function to return numbers associated with each color
def count_colors(colors):
    color_count = {'red': 0, 'green': 0, 'blue': 0}
    for color in colors:
        if 'red' in color:
            red = ''
            for i in color:
                if i.isnumeric():
                    red += i
            color_count['red'] = int(red)

        if 'green' in color:
            green = ''
            for i in color:
                if i.isnumeric():
                    green += i
            color_count['green'] = int(green)

        if 'blue' in color:
            blue = ''
            for i in color:
                if i.isnumeric():
                    blue += i
            color_count['blue'] = int(blue)

    return color_count

#### MAIN CODE ####

red_possible = 12
green_possible = 13
blue_possible = 14

# Open the file and place each line in a list
with open('day2_cube_conundrum/puzzle_input2.txt', 'r') as file:
    raw_data = file.read()
    data = raw_data.split('\n')

print(count_colors(split_games_into_rounds(data[0])[1].split(', ')))
