def countcow():
	for i in range(800,1000):
		if (i-2) % 9 == 0 and (i-3) %13 ==0:
			print i

#countcow()
print 'There are %03d oranges in the basket' % 32
print '1'*10 + '%d' %32
class Solution(object):
	def findPeakElement(self, nums):
		"""
        :type nums: List[int]
        :rtype: int
		"""
		for i in range(1,len(nums)-1):
			if nums[i] > nums[i-1] and nums[i] < nums[i+1]:
				return i


