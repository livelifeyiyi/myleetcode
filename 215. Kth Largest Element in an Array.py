class Solution(object):
	#42ms
	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		n = len(nums)
		nums.sort()
		return nums[n-k]
		# convert the kth largest to smallest
		#return self.findKthSmallest(nums, len(nums)+1-k)
S =Solution()
print S.findKthLargest([3,2,1,5,6,4],2)