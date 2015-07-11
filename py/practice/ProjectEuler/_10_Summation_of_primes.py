# -*- coding: utf-8 -*-
#https://projecteuler.net/problem=10
import unittest
import time
from _3_Largest_prime_factor import miller_rabbin

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n > 2 and n & 1 == 0:
        return False

    flag = True
    i = 3
    while i * i <= n:
        if n % i == 0:
            flag = False
            break
        i = i + 2
    return flag

def normal_solution():
    sum = 0
    for i in range(1, 2000000):
        if is_prime(i):
            sum = sum + i
    return sum

def miller_rabbin_solution():
    sum = 0
    for i in range(1,2000000):
        if miller_rabbin(i):
            sum = sum + i

    return sum

if __name__ == '__main__':

    start = time.time()
    sum = normal_solution()
    end = time.time()
    print("result is {0}".format(sum))
    print("time cost of normal solution is {0}".format(end - start))

    start = time.time()
    sum = miller_rabbin_solution()
    end = time.time()
    print("result is {0}".format(sum))
    print("time cost of miller_rabbin solution is {0}".format(end - start))

    print(sum)