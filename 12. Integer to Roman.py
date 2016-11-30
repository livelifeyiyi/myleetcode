class Solution(object):
	def intToRoman(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		res = ''
		#d = {0:'', 1:'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
		#keys = [5,10,50,100,500,1000]
		d = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
		keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
		if num:	
			print num
			'''if num:
				for i in d.keys():
					for j in d.keys():
						if int(i) - num == int(j):
							res += d[j] + d[i]
							return res
						elif int(i) + int(j) == num:
							(i, j) = (max(i,j), min(i,j))
							res += d[i] + d[j]
							return res'''
			for k in range(0, len(keys)):
				#if (num / keys[k]) > 0 and (num / keys[k]) < 4 and (num / keys[k+1]) <= 0:
				print keys[k]
				res += d[keys[k]] * (num / keys[k])
				num -= keys[k] * (num / keys[k])
		return res
	def intToRoman2(self, num):
		dict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
		ret = ''
		for i in dict.keys():
			ret += (num//i)*dict[i]
			num -= (num//i)*i
		return ret	
	def intToRoman3(self, num):
		M = ["", "M", "MM", "MMM"];
		C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
		X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
		I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
		return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];
s = Solution()
print s.intToRoman(99)
