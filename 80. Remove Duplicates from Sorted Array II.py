class Solution(object):
	def removeDuplicates1(self, nums):
		"""
		:type nums: List[int],sorted
		:rtype: int, length
		"""
		if len(nums) <= 2:
			return len(nums)
		resarr = [nums[0]]
		i = 1
		while i < len(nums):
			if nums[i] == resarr[-1]:
				if resarr.count(nums[i]) < 2:
					resarr.append(nums[i])
				else:
					while i < len(nums) and nums[i] == resarr[-1]:
						i += 1
					continue
			else:
				resarr.append(nums[i])
			i += 1
		print resarr
		return len(resarr)
	def removeDuplicates2(self, nums):
		if len(nums) <= 2:
			return len(nums)
		i, j, k = 0, 1, 2
		while k < len(nums):
			if nums[i] == nums[j] == nums[k]:
				nums.pop(k)
			else:
				i += 1
				j += 1
				k += 1
		#print nums
		return len(nums)
	def removeDuplicates3(self, nums):
		i = 0
		for num in nums:
			if i < 2 or num > nums[i - 2]:
				nums[i] = num
				i += 1
		print nums
		return i

s = Solution()
print s.removeDuplicates3([1,1,1,1,2])