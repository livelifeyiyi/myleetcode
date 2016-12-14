class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		diction = {'1':[''], '2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z'], '0':['']}
		n, res = len(digits), []
		if n == 0: return res
		#print lambda acc, digit: [x+y for x in acc for y in diction[digit]]
		return reduce(lambda acc, digit: [x+y for x in acc for y in diction[digit]], digits, [''])

	def letterCombinations2(self, digits):
		diction = {'1':[''], '2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z'], '0':['']}
		n, res = len(digits), ['']
		if n == 0: return []
		for i in range(n):
			tmp = []
			for y in res:
				for letter in diction[digits[i]]:
					tmp.append(y + letter)
			res = tmp
			print res
		return res
s = Solution()
print s.letterCombinations('2')

