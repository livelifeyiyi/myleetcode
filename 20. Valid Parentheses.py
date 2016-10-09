#!usr/bin/python
#-*- coding UTF-8 -*-
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {'(':')','[':']','{':'}'}
        begin = ['(','{','[']
        end = [')','}',']']
        for i in s:
            if i in begin:
                stack.append(i)
            if i in end:
                if len(stack) == 0:
                    return False
                t = stack.pop()
                print t
                
                if match[t] != i:
                    return False
        if len(stack) > 0:
            return False
            
        else:
            return True

S = Solution()
print S.isValid('[]()')