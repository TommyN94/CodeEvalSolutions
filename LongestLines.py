# Longest Lines
#
# https://www.codeeval.com/open_challenges/2/
#
# Challenge Description: Write a program which reads a file and prints to 
# stdout the specified number of the longest lines that are sorted based on 
# their length in descending order.
import sys


input_file = sys.argv[1]
with open(input_file, 'r') as test_cases:
    number_of_lines_to_print = int(test_cases.readline().rstrip())
    lines = []
    for case in test_cases:
        lines.append(case.rstrip())
        
lines.sort(key=len, reverse=True)
for l in lines[:number_of_lines_to_print]:
    print(l)
