#!/usr/bin/python
from math import factorial

# This seems to be the fastest solution.
sum = 0
for l in str(factorial(100)):
    sum += int(l)
print sum