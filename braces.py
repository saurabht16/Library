#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the braces function below.
def braces(values):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    res = []
    for val in values:
        s = []
        for v in val:
            if v in open_list:
                s.append(v)
            elif v in close_list:
                pos = close_list.index(v)
                if ((len(s) > 0) and (open_list[pos] == s[len(s)-1])):
                    s.pop()
                else:
                    res.append("NO")
                    break

        else:
            if len(s) == 0:
                res.append("YES")
            else:
                res.append("NO")
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    values_count = int(input())

    values = []

    for _ in range(values_count):
        values_item = input()
        values.append(values_item)

    res = braces(values)

    fptr.write('\n'.join(res))
    fptr.write('\n')

    fptr.close()