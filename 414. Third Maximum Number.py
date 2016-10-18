class Solution(object):
	def thirdMax(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums: return []
		nums = list(set(nums))
		nums.sort()
		if len(nums) >=3: return nums[-3]
		elif len(nums) == 2: return nums[-1]
		else: return nums[0]
s =Solution()
print s.thirdMax()