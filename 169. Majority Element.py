import math
class Solution(object):
	def majorityElement(self, nums):
		#halfnum = len(nums) / 2 + (lambda x: 1 if len(nums) % 2 ==0 else 0)
		halfnum = math.floor(len(nums) / 2.0)
		print halfnum
		new = set(nums)

		for obj in new:
			if nums.count(obj) > halfnum:
				return obj
			continue

S =Solution()
print S.majorityElement([1,2,1])
