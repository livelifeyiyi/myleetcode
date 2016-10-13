class Solution(object):
	def __init__(self):
		self.allnum = []
	def isHappy(self, n):
		print n
		strn = str(n)
		self.allnum.append(n)
		sum = 0
		for i in range(len(strn)):
			sum += pow(int(strn[i]), 2)
		if sum in self.allnum and sum != 1:
			return False
		else:
			return True if sum == 1 else self.isHappy(sum)

S = Solution()
print S.isHappy(1)