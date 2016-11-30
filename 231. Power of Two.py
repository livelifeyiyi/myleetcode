import math
class Solution(object):
	def isPowerOfTwo(self, n):
		if n <= 0: return False
		#if not n & n-1: return True
		#faster method:
		#if (math.log10(n) / math.log10(2)).is_integer(): return True
		if math.sqrt(n).is_integer(): return True
		else: return False

	def isPowerOfThree(self, n):
		'''
		return n > 0 and 1162261467 % n == 0
		'''
		if n <= 0: return False
		if (math.log10(n) / math.log10(3)).is_integer():
			return True
		else:
			return False
S = Solution()
print S.isPowerOfThree(27)