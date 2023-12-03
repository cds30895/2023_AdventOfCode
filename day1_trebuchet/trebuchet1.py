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

# For each number, slice the first and last character and combine them
# to find the missing calibration_values, typecasting as integers
calibration_values = []

for item in nums:
    new_num = ''
    new_num += item[0]
    new_num += item[-1]
    calibration_values.append(int(new_num))

# Add all calibration_values together and print the sum total
total = 0
for item in calibration_values:
    total += item

print(total)