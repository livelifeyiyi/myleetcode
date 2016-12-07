class Solution(object):
	
	#TLE
	def minSubArrayLen(self, s, nums):
		"""
		:type s: int
		:type nums: List[int]
		:rtype: int
		"""
		if not nums: return 0
		if len(nums) == 1 and nums[0] < s:
			return 0
		#nums.sort() #if use sort, the return is not a subarray
		if max(nums) >= s:
			return 1
		sublen = 2
		while sublen <= len(nums):
			i = 0
			while i+sublen <= len(nums):
				if sum(nums[i:i+sublen]) >= s:
					return sublen
				i += 1
			sublen += 1
		return 0

	def minSubArrayLen2(self, s, nums):
		firstPos = 0
		sumNum = 0
		minlength = len(nums) +1
		for i in xrange(len(nums)):
			sumNum += nums[i]
			while sumNum >= s:
				minlength = min(minlength, i - firstPos+1)
				
				sumNum -= nums[firstPos]
				firstPos += 1
		return minlength
	#sliding windows O(n)
	def minSubArrayLen3(self, s, nums):
		if not nums: return 0
		if sum(nums) < s:
			return 0
		if max(nums) >= s:
			return 1
		left = right = 0
		len_nums = len(nums)
		minlength = len_nums +1
		totalNum = 0
		while right < len_nums:
			totalNum += nums[right]
			right += 1
			while right < len_nums and totalNum < s:
				totalNum += nums[right]
				right += 1
			while totalNum - nums[left] >= s and left < right:
				totalNum -= nums[left]
				left += 1
			minlength = min(minlength, right - left)
		return minlength 

#from testdata import data2
#print len(data2)
s = Solution()
print s.minSubArrayLen3(3, [1,1])
	#120331635,data2)
	#697439,data)
	#120331635
#132
