"""
Advent of Code Day 1: Trebuchet - Puzzle 1
Author: Chris Smith
Description: This code will take alphanumeric input and parse the numbers from each line,
    combining the first and last digits present in each line.  Then it will add the
    numbers generated from each line to output one sum.
"""


# Open the file and place each line in a list
with open('day1_trebuchet/puzzle_input1.txt', 'r') as file:
    raw_data = file.read()
    data = raw_data.split('\n')

# Filter out all alpha characters, leaving only numeric characters
nums = []

for item in data:
    new_string = ''
    for char in item:
        if char.isnumeric():
            new_string += char

    nums.append(new_string)

