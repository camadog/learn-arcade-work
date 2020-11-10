import re

# This function takes in a line of text and returns
# a list of words in the line.
def split(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

dictionary = []
file = open("dictionary.txt")
for line in file:
    line = line.strip()
    dictionary.append(line)
file.close()

# Linear search
print("--- Linear Search ---")

file = open("AliceInWonderLand200.txt")

line_number = 0

for line in file:
    line_number += 1
    line = line.strip()
    words = split(line)
    for word in words:
        i = 0
        while i < len(dictionary) and dictionary[i] != word.upper():
            i += 1
        if i == len(dictionary):
            print("Line:", line_number, "Misspelled word:", word)

file.close()


# Binary search
print("--- Binary  Search ---")

file = open("AliceInWonderLand200.txt")

line_number = 0

for line in file:
    line_number += 1
    line = line.strip()
    words = split(line)

    for word in words:

        lower_bound = 0
        upper_bound = len(dictionary)
        found = False

        while lower_bound <= upper_bound and not found:
            middle_pos = (lower_bound + upper_bound) // 2
            if dictionary[middle_pos] < word.upper():
                lower_bound = middle_pos + 1
            elif dictionary[middle_pos] > word.upper():
                upper_bound = middle_pos - 1
            else:
                found = True

        if not found:
            print("Line", line_number, "possible misspelled word:", word)

file.close()
