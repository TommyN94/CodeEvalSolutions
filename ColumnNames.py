# Column Names
#
# https://www.codeeval.com/open_challenges/197/
# 
# Challenge Description: Microsoft Excel uses a special convention to name its
# column headers. The first 26 columns use the letters 'A' to 'Z'. Then, Excel
# names its column headers using two letters, so that the 27th and 28th column
# are 'AA' and 'AB'. After 'ZZ', Excel uses three letters.
#
# Write a function that takes as input the number of the column, and returns 
# its header. The input will not ask for a column that would be greater than 
# 'ZZZ'.
import string
import sys


def col_num_to_excel_header(number):
    assert number > 0
    if number <= 26:
        return string.ascii_uppercase[number - 1]
    else:
        quotient = number // 26
        remainder = number % 26
        if remainder == 0:
            return col_num_to_excel_header(quotient - 1) + col_num_to_excel_header(26)
        else:
            return col_num_to_excel_header(quotient) + col_num_to_excel_header(remainder)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if not test == '\n':
        test_number = int(test.rstrip())
        print(col_num_to_excel_header(test_number))
test_cases.close()

sys.exit(0)
