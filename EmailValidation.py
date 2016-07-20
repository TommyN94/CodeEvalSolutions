# Email Validation
# 
# https://www.codeeval.com/open_challenges/35/
#
# Challenge Description: You are given several strings that may/may not be
# valid emails. You should write a regular expression that determines if the
# email id is a valid email id or not. You may assume all characters are from
# the english language.
import re
import sys


def is_valid_email_address(email_address):
    pattern = re.compile(r'.{1,64}@.{1,255}\.[a-z]+')
    return re.match(pattern, email_address) is not None

input_file = sys.argv[1]
test_cases = open(input_file, 'r')

for case in test_cases:
    if case != '\n':
        valid = is_valid_email_address(case.rstrip())
        print(str(valid).lower())


test_cases.close()
sys.exit(0)
