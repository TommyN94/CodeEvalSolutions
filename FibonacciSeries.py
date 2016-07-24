import sys

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

input_file = sys.argv[1]
with open(input_file, 'r') as test_cases:
    for case in test_cases:
        number = int(case.rstrip())
        print(fibonacci(number))
sys.exit(0)
