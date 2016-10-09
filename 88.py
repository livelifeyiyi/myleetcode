class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        lens = m
        len1 = len(nums1)
        len2 = len(nums2)
        while len1 > m:
            nums1.pop(len1-1)
            len1 -= 1
        while len2 > n:
            nums2.pop(len2-1)
            len2 -= 1   
        #print nums1,nums2 
        
        if m > 0 and n > 0:
            if nums1[m-1] < nums2[0]:
                nums1= nums1 + nums2
            elif nums1[0] > nums2[n-1]:
                nums1= nums2 + nums1
            else:
                while i < lens and j < n:
                    if nums1[i] > nums2[j]:
                        nums1.insert(i,nums2[j])
                        lens += 1
                        i += 1
                        j += 1
                    i += 1
                
                while lens < m+n:
                    nums1.insert(i,nums2[j])
                    lens += 1
                    i += 1
                    j += 1
        else:nums1[:n] = nums2[:n]
        return nums1        

    def merge2(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            
        nums1[:n] = nums2[:n]
        return nums1
S = Solution()
print S.merge([1,0],1,[2],1)
