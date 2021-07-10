# import math
# import os
# import random
# import re
# import sys


def solve(s):
    is_first_w = False
    for i in range(len(s)):
        if i == 0 and s[i] != ' ':
            s = s[:i] + s[i].upper() + s[i + 1:]
        if is_first_w and s[i] != ' ':
            s = s[:i] + s[i].upper() + s[i + 1:]
            is_first_w = False
        if s[i] == ' ':
            is_first_w = True
    return s


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input('')
    result = solve(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()


if __name__ == '__main__':
    main()
