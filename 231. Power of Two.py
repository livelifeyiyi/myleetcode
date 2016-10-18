import math
class Solution(object):
	def isPowerOfTwo(self, n):
		if n <= 0: return False
		#if not n & n-1: return True
		#faster method:
		if (math.log10(n) / math.log10(2)).is_integer(): return True
		else: return False
S = Solution()
print S.isPowerOfTwo(19)