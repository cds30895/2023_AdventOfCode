"""
Advent of Code Day 1: Trebuchet - Puzzle 2
Author: Chris Smith
Description: This code will take alphanumeric input and parse the numbers from each line,
    both in digit and alpha form.  It will then combine the first and last number of each
    item and give the sum of all items.
"""

# Function to replace alpha representations of numbers with their numeric counterparts
def replace_alpha_with_num(item, written_numbers, nums):
    for i, alphanum in enumerate(written_numbers):
        item = item.replace(alphanum, str(nums[i]))
    return item

written_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
nums = range(1, 10)
replaced_data = []

# Open the file and place each line in a list
with open('day1_trebuchet/puzzle_input1.txt', 'r') as file:
    raw_data = file.read()
    data = raw_data.split('\n')


# For each item, replace alphas with nums and append to new list
for item in data:
    replaced_data.append(replace_alpha_with_num(item, written_numbers, nums))



# Filter out all alpha characters, leaving only numeric characters
nums = []

for item in replaced_data:
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