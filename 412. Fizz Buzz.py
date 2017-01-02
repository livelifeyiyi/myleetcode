class Solution(object):
	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		#return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
		res = []
		outstr = ''
		for i in range(1, n+1):
			if i % 15 == 0:
				outstr = 'FizzBuzz'
			elif i % 3 == 0:
				outstr = 'Fizz'
			elif i % 5 == 0:
				outstr = 'Buzz'
			else: outstr = '%s' % i
			res.append(outstr)
		return res
s = Solution()
print s.fizzBuzz(15)