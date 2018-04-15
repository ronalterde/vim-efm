#!/usr/bin/env python3
"""Find all occurences of 'needle' in haystack

(simulating a long database query)

Example: query_match.py haystack.txt foo

"""

import sys
import time

def find_all(in_str, pattern):
    positions = []
    pos = 0
    while True:
        pos = in_str.find(pattern, pos)
        if pos == -1:
            break
        positions.append(pos)
        pos += len(pattern)
    return positions

if __name__ == "__main__":
    haystack_filename = sys.argv[1]
    needle = sys.argv[2]

    time.sleep(10)

    with open(haystack_filename, 'r') as f:
        lineNo = 1
        for line in f.readlines():
            positions = find_all(line, needle)
            for columnNo in positions:
                print('{}:{}:{}'.format(haystack_filename, lineNo, columnNo+1))
            lineNo += 1
