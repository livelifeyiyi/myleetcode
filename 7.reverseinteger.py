#-*- coding: utf-8 -*-
#######别人的代码：
'''
def reverse(x):
    sign = -1 if x<0 else 1
    res, x = 0, abs(x)
    while x:
        res = res*10 + (x%10)
        x /= 10
    # handle the overflow bound
    if res > 2**31+1 or res < -2**31-1:
        return 0
    return res*sign
'''
##########################
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sig = -1 if x<0 else 1
        x=x*sig
        strx = str(x)
        lens = len(strx)
        arr = []
        arr = strx[:]
        rearr = [[]for i in range(lens)]
        for i in range(0,lens):
            rearr[lens-1-i].append(arr[i]) 
        restr = ''
        for i in range(0,lens):
            restr1 = ''.join(rearr[i])
            restr = restr + restr1
        reint = int(restr) *sig
           
        if reint > 2**31+1 or reint < -2**31-1:
            return 0
        else:
            return reint


s=Solution()
print s.reverse(1534236469)