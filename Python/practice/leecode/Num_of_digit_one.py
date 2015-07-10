class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
    	if n <= 0:
    		return 0

    	digit = 1
    	i = 1
    	sum = 0
    	while  n // (10**(i-1)) != 0:
    		sum = sum + self.countDigitOneFromIth(n, i, digit)
    		i = i + 1
    	return sum

    def countDigitOneFromIth(self, n, i, k):
    	div = 10**i
    	left = n // div
    	right = n % div
    	sum = left * (10**(i-1))

    	if right >= (k+1)*(10**(i-1)):
    		sum = sum + (10**(i-1))
    	elif right >= k*(10**(i-1)):
    		sum = sum + right % (10**(i-1)) + 1

    	print("sum on the {0}th digit is {1}".format(i, sum))
    	return sum

s = Solution()
print(s.countDigitOne(13))