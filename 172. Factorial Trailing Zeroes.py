class Solution(object):
	def trailingZeroes(self, n):
		return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)
'''
Because all trailing 0 is from factors 5 * 2.
But sometimes one number may have several 5 factors, for example, 25 have two 5 factors, 125 have three 5 factors. I
n the n! operation, factors 2 is always ample. So we just count how many 5 factors in all number from 1 to n.'''

#still Time Limit Exceeded
class Solution2(object):
	def trailingZeroes(self, n):
		count = 0
		for i in xrange(1, n+1):
			j = i
			while j % 5 == 0:
				count += 1
				j /= 5
			continue
		return count

#Time Limit Exceeded
class Solution1(object):
	def trailingZeroes(self, n):
		fac, count= 1,0
		for i in range(1, n+1):
			fac = fac * i
		facstr = str(fac)
		lens = len(facstr)
		for i in range(lens):
			if facstr[lens -1 -i] == '0':
				count += 1
			else: return count
S = Solution()
print S.trailingZeroes(25)