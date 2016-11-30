class Solution(object):
	#TLE
	def minMoves(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		step = 0
		while True:
			if len(set(nums)) == 1:
				return step
			nums.sort()
			for i in range(0, len(nums)-1):
				nums[i] += 1
			step += 1
		return step
	def minMoves2(self, nums):
		min_num = min(nums)
		return sum(x - min_num for x in nums)
s = Solution()
print s.minMoves2([1,9])
