class Solution(object):
	def threeSumClosest1(self, nums, target):
		"""
		for sub array
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		nums.sort()
		min_sum = abs(sum(nums[0:3])-target)
		res = None
		for i in range(len(nums) - 2):
			substr = nums[i:i+3]
			sumval = sum(substr)
			if res != None and abs(sumval-target) > min_sum:
				break
			#print substr
			if abs(sumval-target) <= min_sum:
				min_sum = abs(sumval-target)
				res = sumval
		return res
	def threeSumClosest(self, nums, target):
		nums.sort()
		res = nums[0] + nums[1] + nums[len(nums) - 1]
		#res = {}
		
		for i in range(len(nums) - 2):
			left, right = i+1, len(nums) - 1
			while left < right:
				print left, right, i
				sumval = nums[left] + nums[right] + nums[i]
				absval = abs(sumval - target)
				if absval == 0:
					return sumval
				#if res:
				if absval < abs(res - target):
					res = sumval
					#res[absval]= sumval
				if sumval < target:
					left += 1
				if sumval > target:
					right -= 1
		#minres = min(res.keys)
		return res

s = Solution()
print s.threeSumClosest([0,1,2],0)
        