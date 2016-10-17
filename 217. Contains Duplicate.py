#-*- coding: utf-8 -*-
class Solution(object):
	def containsDuplicate(self, nums):
		setnum = set(nums)
		if len(setnum) == len(nums):
			return False
		else: return True

	#tle
	def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		setnum = set(nums)
		dulnum = {}
		for i in setnum:
			if nums.count(i) >= 2:
				dulnum[i] = nums.index(i)
		for i in range(0, len(nums)):
			if nums[i] in dulnum.keys() and i != dulnum[nums[i]] and i - dulnum[nums[i]] <= k:
				return True
				#dulnum[nums[i]].append(i)
			dulnum[nums[i]] = i
			'''lens = len(dulnum[nums[i]])
				if lens > 1:
					if dulnum[nums[i]][lens-1] - dulnum[nums[i]][lens-2] <= k:
						return True
				continue'''
		return False
	#We don't need an array in the hashtable to hold every position of every element we encounter, since we can just hold the LAST
	#position of every distinct integer we encounter.
	#两个相同数的index差小于k
	def containsNearbyDuplicate2(self, nums, k):
		dulnum = {}
		setnum = set(nums)
		if len(setnum) == len(nums):
			return False
		for index, num in enumerate(nums):
			if nums.count(num) < 2:
				continue
			if num in dulnum.keys() and index - dulnum[num] <= k:
				return True
			dulnum[num] = index
		return False

S = Solution()
print S.containsNearbyDuplicate2([1, 0, 1, 2], 1)