"""
Advent of Code Day 3: Gear Ratios
Author: Chris Smith
Description: This program will take a large input of numbers separated by periods and symbols and print
    the sum of all numbers that are adjacent to a symbol horizontally, vertically, or diagonally.
"""

#### CLASSES ####

# The DoubleNode() and DoublyLinkedList() form an architecture in
# which each line can be compared to the line above and below it
class DoubleNode():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.numbers = find_numbers(value)
        self.syms_idx = find_symbols(value)

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

    # Replace all symbols with '.'
    for char in string:
        if char == '.' or char.isnumeric():
            chunks += char
        else:
            chunks += '.'

    # Create a new list split by '.' in order to preserve multi-numeral numbers
    chunks = chunks.split('.')
    
    # Add the preserved numbers to a list, filtering out '.' and ''
    for item in chunks:
        if item != '.' and item != '':
            nums.append(item)

    # Add found numbers as keys to a dictionary with values of a list of indexes the number occupies
    for num in nums:
        found_numbers[num] = list(range(string.index(num), (string.index(num) + len(num))))

    return found_numbers

# Function to return list of indexes of all symbols in a given string
def find_symbols(string):
    syms_idx = []

    # Append indexes of symbols to a list
    for i, char in enumerate(string):
        if char != '.' and not char.isnumeric():
            syms_idx.append(i)

    return syms_idx


#### MAIN CODE ####

dllist = DoublyLinkedList()

# Open the file and place each line in a list
with open('day3_gear_ratios/puzzle_input3.txt', 'r') as file:
    raw_data = file.read()
    data = raw_data.split('\n')

# for line in data:
#     dllist.append(line)

nums = find_numbers(data[0])
syms = find_symbols(data[0])

print(nums)
print(syms)