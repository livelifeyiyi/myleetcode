from collections import Counter
class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		res = odd = 0
		c = Counter(s)
		for i in c:
			num =  c[i]
			if num % 2 == 0:
				res += num
			else:
				res += num-1
				odd = 1

		return res + odd

s = Solution()
print s.longestPalindrome('abccccdd')