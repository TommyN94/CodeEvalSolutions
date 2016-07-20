# Remove Characters
#
# https://www.codeeval.com/open_challenges/13/
#
# Challenge Description: Write a program which removes specific characters from
# a string.
import sys


input_file = sys.argv[1]
test_cases = open(input_file, 'r')

for line in test_cases:
    line_content = line.split(',')
    source_string = line_content[0]
    # After the ',' delimeter there is always whitespace which shouldn't be removed from the source
    # string. Therefore the slicing.
    characters_to_remove = line_content[1][1:]
    for char in characters_to_remove:
        source_string = source_string.replace(char, '')
    print(source_string)

test_cases.close()
sys.exit(0)
