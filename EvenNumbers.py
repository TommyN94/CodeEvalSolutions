# Even Numbers
#
# https://www.codeeval.com/open_challenges/100/
#
# Write a program which checks input numbers and determines whether a number
# is even or not.
import sys


def is_even(number):
    return number % 2 == 0

input_file = sys.argv[1]
with open(input_file, 'r') as test_cases:
    for case in test_cases:
        num = int(case.rstrip())
        if is_even(num):
            print(1)
        else:
            print(0)
sys.exit(0)
