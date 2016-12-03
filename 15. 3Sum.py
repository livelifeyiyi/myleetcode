class Solution(object):
	#TLE
	def threeSum(self, nums):
		"""
		Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
		Find all unique triplets in the array which gives the sum of zero.
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums.sort()
		n = len(nums)
		result = []
		if not nums or nums[n-1] < 0 or nums[0] > 0: return result
		for i in range(0, n-2):
			for j in range(i+1, n-1):
				for k in range(j+1, n):
					if nums[i] + nums[j] + nums[k] == 0:
						val = [nums[i], nums[j], nums[k]]
						if val not in result: result.append(val)
		return result

	def threeSum2(self, nums):
		nums.sort()
		n = len(nums)
		result = []
		if not nums or nums[n - 1] < 0 or nums[0] > 0: return result
		for i in range(0, n - 2):
			left = i + 1
			right = n -1
			if nums[i] == nums[i - 1] and i != 0:
				continue
			num = nums[i]
			while left < right:
				total = nums[right] + nums[left] + num
				if total == 0:
					val = [num, nums[left], nums[right]]
					if val not in result: result.append(val)
					left += 1
					right -= 1
					#skip duplicate values
					while left < right and nums[left] == nums[left-1]:
						left += 1
					while left < right and nums[right] == nums[right+1]:
						right -= 1
				elif total > 0:
					right -= 1
					while left < right and nums[right] == nums[right+1]:
						right -= 1
				else:
					left += 1
					while left < right and nums[left] == nums[left-1]:
						left += 1
		return result
	#TLE
	def threeSum3(self, nums):
		result = []
		for i in range(len(nums)):
			for j in range(i + 1, len(nums)):
				tmp = 0 - nums[j] - nums[i]
				numsj = set(nums[j+1:])
				if tmp in numsj:
					# to keep list sorted in order to remove duplicate
					if sorted([nums[i], tmp, nums[j]]) not in result:
						result.append(sorted([nums[i], tmp, nums[j]]))
		return result

s = Solution()
print s.threeSum3([-1,0,1,2,-1,-4])