class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		res, res2 = [], []
		max = 0
		for i in range(len(s)):
			if s[i] in res:
				res = res[res.index(s[i]) + 1:]
			res.append(s[i])
			res2 = res
			if len(res2) > max: max = len(res2)
		return max
s = Solution()
print s.lengthOfLongestSubstring("pwwkew")