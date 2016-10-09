
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''s1 = set(nums)
        a2 = sum(s1) * 3 - sum(nums)
        print a2/2'''
        nums.sort()
        i = 0
        while i < len(nums)-2:
            if nums[i] == nums[i+1] == nums[i+2]:
                i += 3
            else: return nums[i]
        return nums[i]
        '''for i in nums:
            if nums.count(i) == 1:
                return i
            else: continue'''



S = Solution()
print S.singleNumber([1,2,3,2,2,1,1])
