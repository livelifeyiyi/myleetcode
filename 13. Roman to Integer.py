class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        re = d[s[len(s)-1]]
        for i in range(0,len(s)-1):
            if(d[s[i]]<d[s[i+1]]):
                re -= d[s[i]]
            else:
                re += d[s[i]]
        return re