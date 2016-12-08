class Solution2(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        #return len(s.split())
        if not s:
            return 0
        lists = s.split(" ")
        len = 0
        print lists
        for i in lists:
            if i != '':
                len += 1
        return len
s = Solution2()
print s.countSegments("                ")
