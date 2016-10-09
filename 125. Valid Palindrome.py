import re
class Solution(object):
    def isPalindrome(self, s):
        ### run time error
        """
        :type s: str
        :rtype: bool
        """
        #alphanumeric = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        for i in s:
            if not i.isalnum():
                s = s.replace(i, '')
        half = len(s)/2
        for i in range(0, half):
            if re.match(s[i], s[-i-1], flags=re.IGNORECASE):
                continue
            else:
                return False
        return True
class Solution2(object):
    def isPalindrome(self, s):
        print s[::-1]
        if s == "": return True
        begin = 0
        end = len(s) - 1
        while begin < end:
            while begin < len(s)-1 and not s[begin].isalnum(): begin +=1
            while end > -1 and not s[end].isalnum(): end -= 1
            print s[begin] + "    " + s[end]
            if s[begin].lower() != s[end].lower(): return False
            begin += 1
            end -= 1
        return True
S = Solution()
print S.isPalindrome(".a")
