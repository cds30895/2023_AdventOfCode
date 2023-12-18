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

        # Dictionary with keys of discrete numbers, values of indexes occupied by number with buffer of 1 on either side
        self.numbers = find_numbers(value)

        # List of indexes occupied by symbols
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
            # print(f'Head Node created: {self.head.value}')
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        # print(f'Appended new Node with value: {self.tail.value}')

    def adjacent_numbers(self):
        adjacent_numbers = []
        node = self.head

        # Separate loop for head node
        for num, num_idx in node.numbers.items():
            for idx in num_idx:
                if idx in node.syms_idx or idx in node.next.syms_idx:
                    adjacent_numbers.append(num)
                    break
        node = node.next

        while node.next is not None:
            for num, num_idx in node.numbers.items():
                for idx in num_idx:
                    if idx in node.prev.syms_idx or idx in node.syms_idx or idx in node.next.syms_idx:
                        adjacent_numbers.append(num)
                        break
            
            node = node.next

        # Separate loop for tail node
        for num, num_idx in node.numbers.items():
            for idx in num_idx:
                if idx in node.prev.syms_idx or idx in node.syms_idx:
                    adjacent_numbers.append(num)
                    break
        
        return adjacent_numbers


#### FUNCTIONS ####

# Function to return dictionary of all numbers and their indexes in a given string
def find_numbers(string):
    chunks = ''
    nums = []
    nums_idx = []
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

# Function to return list of indexes of all symbols in a given string
def find_symbols(string):
    syms_idx = []

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

for line in data:
    dllist.append(line)

