#!/usr/bin/env python3

import sys


day_prev, black_won_count = None, 0
for line in sys.stdin:
    day, black_won = line.strip().split('\t')
    if day_prev is not None and day == day_prev:
        black_won_count += int(black_won)
    else:
        if day_prev is not None:
            print("{}\t{}".format(day_prev, black_won_count))
        day_prev = day
        black_won_count = int(black_won)
if day_prev is not None:
    print(day_prev, black_won_count)
