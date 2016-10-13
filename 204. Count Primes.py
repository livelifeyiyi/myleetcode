import math
class Solution(object):
	def countPrimes(self, n):
		isPrime = [True] * max(n, 2)
		isPrime[0], isPrime[1] = False, False
		x = 2
		while x * x < n:
			if isPrime[x]:
				p = x * x
				while p < n:
					isPrime[p] = False
					p += x
			x += 1
		return sum(isPrime)

S = Solution()
print S.countPrimes(10)

class Solution2(object):
	def countPrimes(self, n):
		count = 0
		for x in range(2, n):
			if self.issimple(x):
				count += 1
		return count
	def issimple(self, x):
		if x == 2:
			return True
		for y in range(2, x):
			if x % y == 0:
				return False
			if y * 2 > x:
				break
		return True