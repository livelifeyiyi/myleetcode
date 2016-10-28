class Solution(object):
	def findTheDifference(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""

		s = sorted(s)
		t = sorted(t)
		for i in range(len(s)):
			if s[i] != t[i]:
				return t[i]
		return t[len(t)-1]
	def solution2(self):
		redict = dict.fromkeys(set(s), 0)
		for i in t:
			if i in redict:
				redict[i] += 1
				if redict[i] > s.count(i):return i
			else: return i

s = Solution()
print s.findTheDifference('abcd','abcde')