#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        renum = []
        lens = len(nums)
        for i in xrange(0,lens):
            for j in xrange(i+1,lens):
                addnum = nums[i] + nums[j]
                if(addnum == target):
                    renum = [i,j]
        return renum