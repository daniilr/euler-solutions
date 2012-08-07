#!/usr/bin/python
prev = 1
preprev = 0
sum = 0
while True:
    fib = prev + preprev
    if fib >= 4000000:
        break
    if fib % 2 == 0:
        sum += fib
    preprev = prev
    prev = fib

print sum