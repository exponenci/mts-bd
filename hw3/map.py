#!/usr/bin/env python

import sys


for line in sys.stdin:
    line = line.strip().split(',')[:5]
    if line[0].strip() == 'Blitz tournament' and len(line[3]) > 0 and len(line[4]) > 3:
        day = line[4][8:]
        black_won = 0 if line[3][-1] == '0' else 1
        print("{}\t{}".format(day, black_won))
