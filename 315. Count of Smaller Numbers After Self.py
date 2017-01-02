class Solution(object):
	#TLE
	def countSmaller(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		res =[]
		def count(nums, num):
			smaller = 0
			for i in nums:
				if i < num: smaller += 1
			return smaller
		for i, num in enumerate(nums):
			res.append(count(nums[i:], num))
		return res
'''
import bisect
class Solution(object):
    def countSmaller(self, nums):
        result = []
        sortedList = []
        for num in nums[::-1]:
            position=bisect.bisect_left(sortedList, num)
            result.insert(0,position)
            bisect.insort(sortedList,num)
        return result
        '''
S = Solution()
print S.countSmaller([5,2,6,1])