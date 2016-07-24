# N Mod N
#
# https://www.codeeval.com/open_challenges/62/
#
# Given two integers N and M, calculate N Mod M (without using any inbuilt 
# modulus operator).
import sys


def mod(x, y):
    if y == 0:
        raise ZeroDivisionError
    while x >= y:
        x -= y
    return x
    
input_file = sys.argv[1]
with open(input_file, 'r') as test_cases:
    for case in test_cases:
        n, m = [int(x) for x in case.rstrip().split(',')]
        print(mod(n, m))
sys.exit(0)
