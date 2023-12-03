"""
Advent of Code Day 1: Trebuchet - Puzzle 2
Author: Chris Smith
Description: This code will take alphanumeric input and parse the numbers from each line,
    both in digit and alpha form.  It will then combine the first and last number of each
    item and give the sum of all items.
"""

# Open the file and place each line in a list
with open('day1_trebuchet/puzzle_input1.txt', 'r') as file:
    raw_data = file.read()
    data = raw_data.split('\n')