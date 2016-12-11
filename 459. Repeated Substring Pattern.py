class Solution(object):
	def repeatedSubstringPattern(self, str):
		"""
		:type str: str
		:rtype: bool
		"""
		#return str in (str*2)[1:-1]
		def computePrefixFunction(pattern):
			m = len(pattern)
			func = [0] * m
			length = 0
			for q in range(1, m):
				while length > 0 and pattern[length] != pattern[q]:
					length = func[length-1]
				if pattern[length] == pattern[q]:
					length += 1
				func[q] = length
			return func
		func = computePrefixFunction(str)
		print func
		n = len(str)
		lenn = func[-1]
		if lenn and n % (n-lenn) == 0:
			return True
		else: return False

s = Solution()
print s.repeatedSubstringPattern('abcabcabc')