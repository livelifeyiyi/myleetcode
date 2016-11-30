class Solution(object):
	def addDigits(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		while num:
			strnum = str(num)
			n = len(strnum)
			if n == 1:
				return num
			num = 0
			for i in range(0,n):
				num += int(strnum[i])
		return num
		#or:
		#return self.addDigits(sum([int(d) for d in list(str(num))]))
	def addDigits2(self, num):
		return num if num <10 else self.addDigits(num % 10 + self.addDigits(num/10))
s = Solution()
print s.addDigits2(38)

    