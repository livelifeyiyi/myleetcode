class Solution(object):
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		#nums.sort()
		num0 = nums.count(0)
		num1 = nums.count(1)
		num2 = nums.count(2)
		for i in range(0,num0):
			nums[i] = 0
		for i in range(0, num1):
			nums[i+num0] = 1
		for i in range(0,num2):
			nums[i+num0+num1] = 2
		num = [0 for i in range(num0)]
		num.extend([1 for i in range(num1)])
		num.extend([2 for i in range(num2)])
		print num
		print nums
	def sortColors2(self, nums):
	    i = j = 0
	    for k in xrange(len(nums)):
	        v = nums[k]
	        nums[k] = 2
	        if v < 2:
	            nums[j] = 1
	            j += 1
	        if v == 0:
	            nums[i] = 0
	            i += 1
	    print nums
	def sortColors3(self, nums):
		i = j = 0
		n = len(nums) - 1
		while j < n:
			if nums[j] < 1:
				nums[i], nums[j] = nums[j], nums[i]
				i += 1
				j += 1
			elif nums[j] > 1:
				nums[j], nums[n] = nums[n], nums[j]
				n -= 1
			else: j += 1
		print nums

s = Solution()
s.sortColors3([1,0,2,1,0])