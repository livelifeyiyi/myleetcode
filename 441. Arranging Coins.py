import math
class Solution(object):
	def arrangeCoins(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n == 0: return 0
		layer = 1
		i = sum = 1
		while sum:
			if sum > n:
				return i-1
			elif sum == n:
				return i
			i += 1
			layer += 1
			sum += i
		return i
	def arrangeCoins2(self, n):
		return int((math.sqrt(1+8*n) - 1)/2)
s = Solution()
print s.arrangeCoins2(8)
