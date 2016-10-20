class Solution(object):
	#TLE
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		n = len(height)
		max = 0
		for i in range(0, n-1):
			for j in range(i+1, n):
				val = min(height[i], height[j]) * (j - i)
				if val > max: max = val
		return max
	def maxArea2(self, height):
		max = curarea = 0
		left, right = 0,  len(height)-1
		while left < right:
			leftlen, rightlen = height[left], height[right]
			if leftlen < rightlen:
				curarea = leftlen * (right - left)
				while height[left] <= leftlen and left < len(height):
					left += 1
			else:
				curarea = rightlen * (right - left)
				while height[right] <= rightlen and right >= 0:
					right -= 1
			if curarea > max: max = curarea
		return max


s = Solution()
print s.maxArea2([1,1])