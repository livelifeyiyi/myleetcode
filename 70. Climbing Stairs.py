#-*- coding:utf-8 -*-
#递归。。时间复杂度太大
class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 1: return 0
        if n == 1: return 1
        if n == 2: return 2
            
        return S.climbStairs(n-1) + S.climbStairs(n-2)

#动态规划
result = [0 for i in range(100)]

class Solution2(object):
    def climbStairs(self, n):
        
        if n == 0: 
            res = 0
            result[n] = res
            return res
        if n == 1: 
            res = 1
            result[n] = res
            return res
        if n == 2: 
            res = 2
            result[n] = res
            return res
            
        if result[n] > 0:
            return result[n]
        else:
            res = S.climbStairs(n-1) + S.climbStairs(n-2)
        result[n] = res
        return res
              
S = Solution2()
print S.climbStairs(35)