class Solution(object):
	def generateParenthesis1(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		#par = ["(",")"]
		def generate(p, left, right, parens=[]):
			if left:
				generate(p + '(', left-1, right)
			if right > left:
				generate(p + ')', left, right-1)
			if not right:
				parens += p,
			return parens
		return generate('', n, n)
	
	def generateParenthesis(self, n, open=0):
		if n == 0: return [')'*open]
		if open == 0:
			return ['('+x for x in self.generateParenthesis(n-1, 1)]
		else:
			return [')'+x for x in self.generateParenthesis(n, open-1)] + ['('+x for x in self.generateParenthesis(n-1, open+1)]
s = Solution()
print s.generateParenthesis(2)