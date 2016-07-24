# Sum of Digits
#
# https://www.codeeval.com/open_challenges/21/
#
# Given a positive integer, find the sum of its constituent digits.
import sys


def sum_of_digits(number):
  digit_sum = 0
  while True:
    remainder = number % 10
    digit_sum += remainder
    number //= 10
    if number == 0:
      break
  return digit_sum

input_file = sys.argv[1]
with open(input_file, 'r') as test_cases:
  for case in test_cases:
    digit_sum = sum_of_digits(int(case.rstrip()))
    print(digit_sum)
sys.exit(0)
