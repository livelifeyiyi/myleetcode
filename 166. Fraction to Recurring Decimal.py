class Solution(object):
	def fractionToDecimal(self, numerator, denominator):
		"""
		:type numerator: int
		:type denominator: int
		:rtype: str
		"""
		res = ''
		remainders = []
		quotients = []
		#result = numerator / denominator
		quotient, remainder = divmod(numerator, denominator)
		while remainder != 0:
			quotients.append(quotient)
			if remainder in remainders: break
			remainders.append(remainder)
			if remainder < denominator:
				remainder = int(str(remainder) + '0')
			quotient, remainder = divmod(remainder, denominator)
		print remainders
		print quotients
s = Solution()
s.fractionToDecimal(2, 3)
