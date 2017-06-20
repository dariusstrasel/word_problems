# Author: Darius Strasel

import itertools

def compare_strings(*args):
    letter_count = {}
    result = []
    for arg in args:
        for character in arg:
            letter_count.setdefault(character, 0)
            letter_count[character] += 1
    for key, value in letter_count.items():
        if int(value) > 1:
            result.append(key)
    return result


first  = compare_strings("SATCHEL", "CLOUD")
second = compare_strings("LOVEBUG", "PROUD")
third = compare_strings("VIPER", "PAVEMENT", "VAMP")
fourth = [char for char in "PIRATE" if char not in "TRAMP"]
fifth = compare_strings("WORLDLY", "DREAM")


print(first)
print(second)
print(third)
print(fourth)
print(fifth)
# ['L', 'C']
# ['U', 'O']
# ['A', 'V', 'E', 'P', 'M']
# ['I', 'E']
# ['R', 'D', 'L']