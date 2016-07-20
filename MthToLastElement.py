# Mth To Last elements
#
# https://www.codeeval.com/open_challenges/10/
#
# Challenge Description: Write a program which determines the Mth to the last 
# element in a list.
import sys


input_file = sys.argv[1]
try:
    test_cases = open(input_file, 'r')
except IOError:
    print('No such file ' + input_file)
    sys.exit(-1)

for line in test_cases:
    line_content = line.split(" ")
    n = len(line_content)
    element_to_print = n - int(line_content.pop()) - 1
    if element_to_print >= 0 and element_to_print < len(line_content):
        print(line_content[element_to_print])

test_cases.close()
sys.exit(0)
