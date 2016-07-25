# Sum Of Integers From File
#
# https://www.codeeval.com/open_challenges/24/
#
# Print out the sum of integers read from a file.
import sys


input_file = sys.argv[1]
with open(input_file, 'r') as test_cases:
    numbers = []
    for case in test_cases:
        num = int(case.rstrip())
        numbers.append(num)
    print(sum(numbers))
sys.exit(0)
