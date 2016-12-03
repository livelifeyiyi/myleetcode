import math
class Solution(object):
	def myPow(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		print math.pow(x,n)
		print pow(x,n)
		print x ** n
		if x == 0: return 0.0
		if n == 0: return 1.0
		if n < 0:
			x = 1/x
			n = -n
		'''res = 1
		while n:
			res *= x
			n -= 1'''
		if n % 2 == 0:
			return self.myPow(x*x, n/2)
		else:
			return x * self.myPow(x*x, n/2)

s = Solution()
print s.myPow(2.2,10)