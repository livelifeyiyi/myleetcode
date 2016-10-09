class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lens = len(nums)
        if lens == 0:
            return 0
        print lens
        i = 0
        j = 0 
        #for i in range(0,lens):
        while(i < lens):
            print nums[i]
            print val
            if int(nums[i]) == val:
                del nums[i]
                lens -= 1
                i -= 1
            i += 1
            print "i="+str(i)+",lens="+str(lens)
            
        return lens

S = Solution()
print S.removeElement([2,3,3,3,3],3)