class Solution(object):
	def wordPattern(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		#set_pat = set(pattern)
		dir = {}
		strlist = str.split(" ")
		if len(pattern) != len(strlist): return False
		if len(set(pattern)) != len(set(strlist)): return False
		for i in range(0, len(pattern)):
			if pattern[i] not in dir.keys(): dir[pattern[i]] = []
			dir[pattern[i]].append(strlist[i])
		for j in dir.keys():
			if len(set(dir[j])) > 1: return False
		return True
s = Solution()
print s.wordPattern("abba", "dog dog dog dog")
