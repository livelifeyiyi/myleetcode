class Solution(object):
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if len(set(s)) != len(set(t)) or len(s) != len(t): return False
		dir = {}
		for i in range(len(s)):
			if s[i] not in dir.keys(): dir[s[i]] = 0
			dir[s[i]] += 1
		for i in range(len(t)):
			if t[i] not in dir.keys() or dir[t[i]] < 1: return False
			dir[t[i]] -= 1
		return True
s = Solution()
print s.isAnagram('a', 'n')
