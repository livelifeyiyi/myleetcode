class Solution(object):
	def moveZeroes(self, nums):
		"""
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
		#dir = list(enumerate(nums))
		#for index, value in enumerate(nums):
		for value in nums:
			if value == 0:
				nums.pop(nums.index(0))
				nums.append(value)
		print nums
s = Solution()
s.moveZeroes([])