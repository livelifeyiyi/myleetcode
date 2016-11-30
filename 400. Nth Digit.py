import math
class Solution(object):
	def findNthDigit(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		width = 1
		n_nums = 9
		num = 1
		pos = 1
		while 1:
			num += n_nums
			pos += n_nums * width
			if pos > n:
				jumps = int(math.ceil(float(pos - n) / width))
				pos -= jumps * width
				num -= jumps
				return int(str(num)[n - pos])
			width += 1
			n_nums *= 10
		return None

s = Solution()
print s.findNthDigit(13)