class Solution(object):
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""        
		res = []
		len1 = len(num1)
		len2 = len(num2)
		ten1 = ten2 = 1
		while len2:
			len1 = len(num1)
			ten1 = ten2
			while len1:
				res.append(int(num1[len1-1]) * int(num2[len2-1]) * ten1)
				len1 -= 1
				ten1 *= 10
			len2 -= 1
			ten2 *= 10
		#print res
		return str(sum(res))
s = Solution()
print s.multiply('23','10')