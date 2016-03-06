class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        print -2**31-1
        print x
        if (x > 2**31+1 or x < -2**31-1 or x < 0):
            return False
        else:
            t = 0 if x>0 else 1
            #print t
            s = str(x)
            lens = len(s)
            #print lens
            j = 0
            for i in range(t,(lens-t)//2+t):
                if(s[i]==s[lens+t-1-i]):
                    j += 1
            if (j == (lens-t)//2):
                return True
            else:
                return False
s=Solution()
print s.isPalindrome(-2147483648)