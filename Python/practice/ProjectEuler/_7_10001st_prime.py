# -*- coding: utf-8 -*-
#https://projecteuler.net/problem=6
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


def GetNextPrime(start, mode="fast"):
    if start <= 2:
        return 2
    elif start & 1 == 0:
        start = start + 1

    while True:
        if mode == "slow":
            if is_prime(start):
                break
        else:
            if miller_rabbin(start):
                break
        start = start + 2
    return start

def GetNthPrime(n, mode="fast"):
    if n <= 0:
        return None

    start = 1
    for i in range(0, n):
        start = GetNextPrime(start+1, mode)
    return start


class  TestGetNthPrime(unittest.TestCase):

    def test_get_nth_prime(self):
        self.assertEqual(GetNthPrime(6), 13)
        self.assertEqual(GetNthPrime(6, mode="slow"), 13)

if __name__ == '__main__':
    #unittest.main()
    start = time.time()
    print(GetNthPrime(10001))
    end = time.time()
    print("Elapsed time is {0}".format(end - start))

    start = time.time()
    print(GetNthPrime(10001, mode="slow"))
    end = time.time()
    print("Elapsed time is {0}".format(end - start))