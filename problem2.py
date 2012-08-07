#!/usr/bin/python
prev = 1
preprev = 0
sum = 0
fib = 0
while fib >= 4000000:
    fib = prev + preprev
    if fib % 2 == 0:
        sum += fib
    preprev = prev
    prev = fib

print sum