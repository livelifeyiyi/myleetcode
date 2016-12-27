class Solution(object):
	#TLE
	def maxSubArray1(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		maxsum = max(nums)
		for gap in range(2,n+1):
			for i in range(0, n-gap+1):
				subnums = nums[i:i+gap]
				maxsum = max(maxsum, sum(subnums))
		return maxsum
	def maxSubArray(self, nums):
		ans = nums[0]
		maxsum = 0
		for i in range(0,len(nums)):
			maxsum += nums[i]
			ans = max(maxsum, ans)
			#print i,ans,maxsum
			maxsum = max(maxsum, 0)
		return ans
S =Solution()
print S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])	
	#[-2,1,-3,4,-1,2,1,-5,4])	