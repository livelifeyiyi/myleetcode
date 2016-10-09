class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if( len(nums) <= 1 ):
            return 0 if not nums else 1
        a,b = 0,1
        while b < len(nums):
            print len(nums)
            #for i in range(0,len(nums)):
            #print nums[i]
            #if(nums[i+1]):
            if( nums[a] == nums[b] ):
                nums.pop(a)
                print nums
                #i = i + 2
            else:
                a = a + 1
                b = b + 1
            print a
            print b
        return len(nums)

S = Solution()
print S.removeDuplicates([1,1,1])