class Solution(object):
	def isScramble(self, s1, s2):
		"""
		:type s1: str
		:type s2: str
		:rtype: bool
		"""
		def getScramble(s1, s2, res):
			if (s1,s2) in res.keys():
				return res[(s1,s2)]
			if not sorted(s1) == sorted(s2):
				return False
			if len(s1) == 1:
				return s1 == s2
			for i in range(1, len(s1)):
				#left part = right part and right = left or left = left and right = right
				if getScramble(s1[:i], s2[-i:], res) and getScramble(s1[i:], s2[:-i], res) or getScramble(s1[:i], s2[:i], res) and getScramble(s1[i:], s2[i:], res):
					res[(s1,s2)] = True
					return True
			res[(s1,s2)] = False
			return False
		res = {}
		return getScramble(s1, s2, res)
		"""l, r = 0, len(s1)
		mid = (l+r) / 2
		left = s1[l: mid][::-1]
		right = s1[mid: r][::-1]
		res += getScramble(left, res)
		res += getScramble(right, res)"""
		
S =Solution()
print S.isScramble('great','rgtae')
