# Swap Case
#
# https://www.codeeval.com/open_challenges/96/
#
# Challenge Description: Write a program which swaps letters' case in a 
# sentence. All non-letter characters should remain the same.
import string
import sys


def swap_case(input_string):
    swapped_string = ''
    for char in input_string:
        if char in string.ascii_lowercase:
            swapped_string += char.upper()
        elif char in string.ascii_uppercase:
            swapped_string += char.lower()
        else:
            swapped_string += char
    return swapped_string


def swap_case2(input_string):
    n_char = len(input_string)
    swapped_characters = [None] * n_char
    for i in range(n_char):
        char = input_string[i]
        if char in string.ascii_lowercase:
            swapped_characters[i] = char.upper()
        elif char in string.ascii_uppercase:
            swapped_characters[i] = char.lower()
        else:
            swapped_characters[i] = char
    return ''.join(swapped_characters)


input_file = sys.argv[1]
test_cases = open(input_file, 'r')

for case in test_cases:
    print(swap_case(case.rstrip()))

test_cases.close()
sys.exit(0)
