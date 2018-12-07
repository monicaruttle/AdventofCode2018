import string
import sys

def find_final_polymer():
    with open('DayFive.txt') as polymer_file:
        polymer = polymer_file.readline()
    
    print(find_polymer_reaction_length(polymer))


def find_polymer_reaction_length(polymer: str):
    i = 0
    while i < len(polymer)-1:
        first = polymer[i]
        second = polymer[i+1]
        if first.lower() == second.lower() and first != second:
            polymer = polymer[:i] + polymer[i+2:]
            if i > 1:
                i -= 2
        else:
            i += 1
    return len(polymer)

def find_troublesome_unit():
    with open('DayFive.txt') as polymer_file:
        polymer = polymer_file.readline()
    
    min_length = sys.maxsize
    for letter in string.ascii_lowercase:
        stripped_polymer = polymer.replace(letter.upper(), '').replace(letter, '')
        length = find_polymer_reaction_length(stripped_polymer)
        if length < min_length:
            min_length = length
    
    print(min_length)


if __name__ == "__main__":
    find_troublesome_unit()