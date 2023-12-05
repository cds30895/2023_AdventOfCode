"""
Advent of Code Day 3: Gear Ratios
Author: Chris Smith
Description: This program will take a large input of numbers separated by periods and symbols and print
    the sum of all numbers that are adjacent to a symbol horizontally, vertically, or diagonally.
"""

#### CLASSES ####

class DoubleNode():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.numbers = find_numbers(value)

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print(f'Head Node created: {self.head.value}')
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print(f'Appended new Node with value: {self.tail.value}')


#### FUNCTIONS ####

# Function to return dictionary of all numbers and their indexes in a given string
def find_numbers(string):
    chunks = ''
    nums = []
    found_numbers = {}

    for char in string:
        if char == '.' or char.isnumeric():
            chunks += char
        else:
            chunks += '.'

    chunks = chunks.split('.')
    
    for item in chunks:
        if item != '.' and item != '':
            nums.append(item)

    for num in nums:
        found_numbers[num] = string.index(num)

    return found_numbers


#### MAIN CODE ####

dllist = DoublyLinkedList()

# Open the file and place each line in a list
with open('day3_gear_ratios/puzzle_input3.txt', 'r') as file:
    raw_data = file.read()
    data = raw_data.split('\n')

# for line in data:
#     dllist.append(line)

nums = find_numbers(data[1])
# for num in nums:
#     if len(num) == 0:

print(nums)
