# Trailing String
# 
# https://www.codeeval.com/open_challenges/32/
# 
# Challenge Description: There are two strings: A and B. Print 1 if string B 
# occurs at the end of string A. Otherwise, print 0.
import sys


def is_trailing_string(x, y):
    return x[-len(y):] == y
    
if __name__ == '__main__':    
    input_file = sys.argv[1]
    with open(input_file, 'r') as test_cases:
        for case in test_cases:
            strings = case.rstrip().split(',')
            if (is_trailing_string(strings[0], strings[1])):
                print(1)
            else:
                print(0) 
