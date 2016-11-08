class Solution(object):
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		res, tem = [], []
		n = len(nums)
		if n < 4: return res
		nums.sort()
		if 4 * nums[0] > target or 4 * nums[n-1] < target:
			return res
		for a in range(0, n - 3):
			if 4 * nums[a] > target or 4 * nums[n - 1] < target:
				break
			for b in range(a + 1, n - 2):
				left = b+1
				right = n-1
				nowtarget = target - nums[a] - nums[b]
				if 2 * nums[left] > nowtarget or 2 * nums[right] < nowtarget:
					continue
				while left < right:
					if nums[left] + nums[right] == nowtarget:
						tem = [nums[a], nums[b], nums[left], nums[right]]
						if tem not in res:
							res.append(tem)
						left += 1
						right -= 1
						while left < right and nums[left] == nums[left - 1]:
							left += 1
						while left < right and nums[right] == nums[right + 1]:
							right -= 1
					if nums[left] + nums[right] < nowtarget:
						left += 1
					if nums[left] + nums[right] > nowtarget:
						right -= 1
		return res
s = Solution()
print s.fourSum([-5,5,4,-3,0,0,4,-2],4)