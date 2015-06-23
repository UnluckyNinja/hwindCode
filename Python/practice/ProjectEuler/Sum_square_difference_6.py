# -*- coding: utf-8 -*-
#https://projecteuler.net/problem=6
import unittest

def GetDelta(start, end):
	sum = 0
	for i in range(start, end):
		for j in range(i+1, end+1):
			sum = sum + 2*i*j

	return sum


class  TestSumSquareDiff(unittest.TestCase):

	def test_sumsquare(self):
		self.assertEqual(GetDelta(1, 10), 2640)

if __name__ == '__main__':
	#unittest.main()

	print(GetDelta(1, 100))