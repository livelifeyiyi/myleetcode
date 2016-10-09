########################
##Solution1: Naive-string-matcher
########################
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        hlen = len(haystack)
        nlen = len(needle)
        print "hlen="+str(hlen)+";nlen="+str(nlen)
        if(hlen == nlen):
            if needle[0:] == haystack[0:]:
                return 0
        print needle[0:nlen]
        for i in range(0, (hlen-nlen+1)):
            
            if needle[0:nlen] == haystack[i:i+nlen]:
                return i
        return -1    

S = Solution()
print S.strStr("mississippi","pi")