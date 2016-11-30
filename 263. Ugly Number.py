class Solution(object):
	def isUgly(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num == 0: return False
		if num == 1: return True
		#list = [2,3,5]
		while(num % 2 == 0):
			num /= 2
		while(num % 3 == 0):
			num /= 3
		while(num % 5 == 0):
			num /= 5
		return num == 1