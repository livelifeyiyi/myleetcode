import math
class Solution(object):
	def divide(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		idea: a / b = e**lna / e**lnb = e**(lna - lnb)
		"""
		int_max = 2**31 -1
		int_min = - 2**31 
		#print int_min
		flag1 = flag2 = 1
		if dividend == 0: return 0
		if divisor == 0: return int_max
		if dividend < 0: 
			dividend = -dividend
			flag1 = -1
		if divisor < 0: 
			divisor = -divisor
			flag2 = -1
		print dividend / divisor
		res = int(math.exp(math.log(dividend, math.e) - math.log(divisor, math.e))) * flag1 * flag2
		return res if res < int_max else int_max
s = Solution()
print s.divide(-2147483648,-1)