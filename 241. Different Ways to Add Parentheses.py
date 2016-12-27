class Solution(object):
	#opr = {'+': operator.add, '-': operator.sub, '*':operator.mul}
	def diffWaysToCompute(self, input):
		"""
		:type input: str
		:rtype: List[int]
		"""
		def opr(op, j, k):
			if op == '+': return j+k
			if op == '-': return j-k
			if op == '*': return j*k
		if input.isdigit():
			return [int(input)]
		res = []
		for i in range(len(input)):
			if input[i] in '+-*':
				res1 = self.diffWaysToCompute(input[:i])
				res2 = self.diffWaysToCompute(input[i+1:])
				for j in res1:
					for k in res2:
						res.append(opr(input[i],j,k))
		return res
S =Solution()
print S.diffWaysToCompute('2*3-4')
