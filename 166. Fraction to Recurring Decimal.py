class Solution(object):
	def fractionToDecimal(self, numerator, denominator):
		"""
		:type numerator: int
		:type denominator: int
		:rtype: str
		"""
		res = ''
		#remainders = []
		quotients = []
		table = {}
		beginrec = ''
		#result = numerator / denominator
		if numerator == 0: return '0'
		if numerator * denominator < 0:
			res += '-'
		numerator = abs(numerator)
		denominator = abs(denominator)
		quotient, remainder = divmod(numerator, denominator)
		#quotients.append(quotient)
		#quotients.append('.')
		res += str(quotient)
		if remainder != 0:res += '.' 
		position = 0
		while remainder != 0:
			if remainder in table.keys(): 
				beginrec = remainder
				break
			#remainders.append(remainder)
			table[remainder] = position
			remainder *= 10
			quotient, remainder = divmod(remainder, denominator)
			quotients.append(quotient)
			position += 1
		if beginrec != '':
			quotients.insert(table[remainder], '(')
			quotients.append(')')
		for i in quotients:
			i = str(i) 
			res += i
		print beginrec
		#print remainders
		print quotients
		print res
		return res
s = Solution()
print s.fractionToDecimal(-2, -5)
