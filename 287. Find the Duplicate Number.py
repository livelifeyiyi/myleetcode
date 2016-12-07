class Solution(object):
	def findDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		for i in nums:
			if nums.count(i) > 1:
				print nums.count(i)
				return i
	def findDuplicate2(self, nums):
		n = len(nums)
		low = 0
		high = n - 1 
		mid = (low + high) / 2
		while low + 1 < high:
			count = 0
			for i in nums:
				if i > mid and i <= high:
					count += 1
			if count > high - mid :
				low = mid
			else: high = mid
			mid = (low + high) / 2
		return high

from testdata import data3
print len(data3)
s = Solution()
print s.findDuplicate2(data3)				