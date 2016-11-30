class Solution(object):
	def addStrings(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		n1 = len(num1)
		n2 = len(num2)
		res = ''
		bit = 0
		while n1 or n2:
			if n1 and n2:
				val = int(num1[n1-1]) + int(num2[n2-1]) + bit
			else:
				if n1:
					val = int(num1[n1-1]) + bit
				if n2:
					val = int(num2[n2-1]) + bit
			if n1 > 0:n1 -= 1
			if n2 > 0:n2 -= 1
			'''if not (n1 == 0 and n2 == 0):
				if val >= 10:
					bit = 1
					val -= 10
				else: bit = 0'''

			res = str(val % 10) + res
			bit = val / 10
		if bit:
			res = str(bit) + res
		return res
s = Solution()
print s.addStrings('1','9')