"""
Advent of Code Day 3: Gear Ratios - Puzzle 2
Author: Chris Smith
Description: This program will take a large input of numbers separated by periods and symbols and print
    the sum of all products of numbers in which two numbers are adjacent to a * symbol.
"""

#### CLASSES ####

# The DoubleNode() and DoublyLinkedList() form an architecture in
# which each line can be compared to the line above and below it
class DoubleNode():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.numbers = self.find_numbers()
        self.gears_idx = self.find_gears()

    def find_numbers(self):
        string = self.value
        chunks = ''
        nums = []
        found_numbers = []

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

        # Add found numbers as tuples with tup[1] values of a list of
        # indexes the number occupies with a buffer of one on each side
        for num in nums:
            if string.index(num) > 0 and string.index(num) != (len(string) - len(num)):
                found_numbers.append((num, list(range((string.index(num) - 1), (string.index(num) + len(num) + 1)))))
                string = string.replace(num, ' ' * len(num), 1)
            elif string.index(num) == 0:
                found_numbers.append((num, list(range(0, (len(num) + 1)))))
                string = string.replace(num, ' ' * len(num), 1)
            elif string.index(num) == (len(string) - len(num)):
                found_numbers.append((num, list(range((string.index(num) - 1), len(string)))))
                string = string.replace(num, ' ' * len(num), 1)
            
        return found_numbers
    
    def find_gears(self):
        gears_idx = []
        
        for i, char in enumerate(self.value):
            if char == '*':
                gears_idx.append(i)

        return gears_idx