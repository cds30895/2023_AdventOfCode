"""
Advent of Code Day 2: Cube Conundrum - Puzzle 2
Author: Chris Smith
Description: Given a game in which cubes are drawn from a bag with an unknown number of cubes,
    this program will determine the minimum number of each color of cube for each game.  These
    minimums will be multiplied to calculate each games "power" and summed to find the total.
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

# Function to list the counts for each round of a game and return the max for each color
def max_count_colors(game):
    max_color_count = {'red': [], 'green': [], 'blue': []}
    rounds = split_games_into_rounds(game)

    for round in rounds:
        color_count = count_colors(split_rounds_into_colors(round))

        for key in color_count.keys():
            max_color_count[key].append(color_count[key])

    for key in max_color_count.keys():
        max_color_count[key] = max(max_color_count[key])

    return max_color_count


# Function to multiply all max_color_count
def mult_count_colors(max_color_count):
    product = 1

    for key in max_color_count.keys():
        product *= max_color_count[key]

    return product


#### MAIN CODE ####

total = 0

# Open the file and place each line in a list
with open('day2_cube_conundrum/puzzle_input2.txt', 'r') as file:
    raw_data = file.read()
    data = raw_data.split('\n')

print(mult_count_colors(max_count_colors(data[0])))
