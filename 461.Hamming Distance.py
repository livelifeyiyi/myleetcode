class Solution(object):
	def hammingDistance(self, x, y):
		"""
		:type x: int
		:type y: int
		:rtype: int
		"""
		#return bin(x^y).count('1')
		distance = 0
		bin_x = bin(x)[2:]#.zfill(32)
		bin_y = bin(y)[2:]#.zfill(32)
		len_x, len_y = len(bin_x), len(bin_y)
		if len_x > len_y:
			bin_y = bin_y.zfill(len_x)
		if len_x < len_y:
			bin_x = bin_x.zfill(len_y)
		#print bin_x, bin_y
		for i in range(0, len(bin_y)):
			if bin_x[i] != bin_y[i]: 
				distance += 1
		return distance
s = Solution()
print s.hammingDistance(1,4)