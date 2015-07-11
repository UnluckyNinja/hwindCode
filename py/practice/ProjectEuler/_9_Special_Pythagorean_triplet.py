# -*- coding: utf-8 -*-
#https://projecteuler.net/problem=9

import sys

for a in range(1, 1000):
	for b in range(a+1, 1000):
		for c in range(b+1, 1000):
			if (a+b+c) == 1000 and (a*a + b*b) == c*c:
				print("hello")
				print ("a={0}, b={1}, c={2}. abc is {3}".format(a, b, c, a*b*c))
				#sys.exit()