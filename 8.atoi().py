
class Solution(object):
	def myAtoi(self, str):
		"""
		:type str: str
		:rtype: int
		"""
		if str == '':
			return 0
		else:
			#reint = int(str)
			i=0
			lens = len(str)
			hasDigit = False
			#i,lens,hasDigit = 0, len(str), False
			while i < lens and str[i] == ' ':
				i += 1
			if i < lens and str[i] in '+-':
				i += 1
			while i < lens and '0'<= str[i] <= '9':
				hasDigit,i = True, i+1
			if not hasDigit: return 0
			result = int(str[:i])
			return -2147483648 if result < -2147483648 else 2147483647 if result > 2147483647 else result

s = Solution()
print s.myAtoi(' 2345')
#s='abc'
#print s[0] 

