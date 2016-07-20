# Lowercase
# 
# https://www.codeeval.com/open_challenges/20/
#
# Challenge Description: Given a string write a program to convert it into
# lowercase.
import sys

input_file = sys.argv[1]
test_cases = open(input_file, 'r')

for case in test_cases:
    print(case.rstrip().lower())

test_cases.close()
sys.exit(0)
