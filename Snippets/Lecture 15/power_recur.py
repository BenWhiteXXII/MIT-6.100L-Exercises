#!/usr/bin/env python3

def power_recur(n, p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    else:
        return power_recur(n*n,p-1)

print(power_recur(2, 3))

# know that x^1 = x
# if x = 2, p = 3
# 2*(2*(2*(2*1)
#
