class Solution(object):
	cache = {}
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		if s == p: 
			self.cache[(s,p)] = True
			return True
		if (s,p) in self.cache: return self.cache[(s, p)]
		if not p: return not s
		if p[-1] == '*':
			if self.isMatch(s, p[:-2]):
				self.cache[(s,p)] = True
				return True
			if s and (p[-2] == s[-1] or p[-2] == '.') and self.isMatch(s[:-1], p):
				self.cache[(s,p)] = True
				return True
		if s and (s[-1] == p[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
			self.cache[(s,p)] = True
			return True
		self.cache[(s,p)] = False
		return False

S = Solution()
print S.isMatch('aab', 'c*a*b')