# -*- coding: utf-8 -*-
#https://projecteuler.net/problem=2

fvalue = [1, 2]
i = 2


def f(i):
    cur = fvalue[i-2] + fvalue[i-1]
    fvalue.append(cur)
    return cur

while f(i) < 4000000:
    i += 1

sum = 0
for item in fvalue:
    if item % 2 == 0:
        sum += item

print(sum)