# -*- coding: utf-8 -*-
#https://projecteuler.net/problem=3
#reference: 
#   1. http://www.cs.colorado.edu/~srirams/classes/doku.php/pollard_rho_tutorial
#   2. http://blog.csdn.net/sr_19930829/article/details/42099667
#   3. http://blog.csdn.net/prime7/article/details/8475183
#   4. http://mathworld.wolfram.com/PollardRhoFactorizationMethod.html
#   5. http://www.cnblogs.com/logichandsome/p/4054543.html
#   6. https://en.wikipedia.org/wiki/Pollard's_rho_algorithm

import random

def gcd(a, b):
    if a == 0 or b == 0:
        return 0

    cur = a % b
    while cur != 0:
        a = b
        b = cur
        cur = a % b

    return b

def multi_mod(a, b, mod):
    a = a % mod
    ret = 0
    while b != 0:
        if b & 1 == 1:
            ret = (ret + a) % mod
        a = (a << 1) % mod
        b = b >> 1
    return ret

def pow_mod(a, n, mod):
    #print("pow_mod {0}^{1}%{2}=".format(a, n, mod))
    ret = 1
    tmp = a % mod
    while n > 0:
        if n & 1 == 1:
            ret = multi_mod(ret, tmp, mod)
        tmp = multi_mod(tmp, tmp, mod)
        n = n >> 1
    #print(ret)
    return ret

def f(x, n):
    return (x * x + 1) % n

def int_fact_rho(n):
    a = b = 2
    while True:
        a = f(a, n)
        b = f(b, n)
        b = f(b, n)
        if a == b:
            a = b = random.randint(2, 10000)
            print ("regenerate a={0} and b={1}".format(a, b))
            continue

        print("HALO a={0} and b={1}".format(a, b))
        c = gcd(abs(a-b), n)
        if c == n:
            return n
        elif c > 1:
            return c

def  check(a, n, x, t):
    #print("check {0}, {1}, {2}, {3}".format(a, n, x, t))
    ret = pow_mod(a, x, n)
    last = ret
    for i in range(t):
        ret = multi_mod(ret, ret, n)
        if ret == 1 and last != 1 and last != (n-1):
            return False
        last = ret

    if ret != 1:
        return False
    return True

def miller_rabbin(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n & 1 == 0:
        return False

    x = n - 1
    t = 0
    while x & 1 == 0:
        x = x >> 1
        t = t + 1

    for i in range(0, 10):
        a = random.randint(2, n-1)
        if check(a, n, x, t) == False:
            return False

    return True

def divide_int(n, list):
    if miller_rabbin(n):
        list.append(n)
        return

    print("try to divide {}".format(n))
    ret = int_fact_rho(n)
    divide_int(ret, list)
    remainder = n // ret
    divide_int(remainder, list)

def divide_int_v2(n, list):
    i = 2
    while n > 1:
        if n % i == 0:
            n = n // i
            list.append(i)
            i = i - 1
        i = i + 1

def main():
    ret = multi_mod(4, 7, 5)
    print(ret)

    ret = pow_mod(9, 3, 100)
    print(ret)

    ret = miller_rabbin(3)
    print(ret)

    ret = miller_rabbin(97)
    print(ret)

    ret = miller_rabbin(93)
    print(ret)

    list = []
    divide_int(31233243214353646, list)
    print(list)
    print(max(list))

if __name__ == '__main__':
    main()
