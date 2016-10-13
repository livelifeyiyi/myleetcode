#-*- coding: utf-8 -*-
class Solution(object):
	def rotate(self, nums, k):
		lens = len(nums)
		k = k % lens
		begin = nums[0:lens-k]
		for i in range(0,lens-k):
			nums.pop(0)
		map(nums.append, begin)
		'''
		this method did not modify nums directly.
		#last = nums[(lens - k):]
		#map(last.append, nums[0:lens-k])
		#nums = last'''
		print nums
	def rotate2(self, nums, k):
		lens = len(nums)
		k = k % lens
		for i in range(k):
			last = nums[-1]
			nums.pop()
			nums.insert(0, last)
		print nums
		nums.reverse()
		print nums
	#三步反转法
	def rotate3(self, nums, k):
		lens = len(nums)
		k = k % lens
		last = nums[(lens - k):]
		for i in range(k):
			nums.pop()
		nums.reverse()
		last.reverse()
		map(nums.append, last)
		nums.reverse()
		print nums

S = Solution()
S.rotate3([1,2,3,4,5,6,7],3)