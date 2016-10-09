class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def nextnum(lastnum):
            strn = str(lastnum)
            #print strn
            restr = ''
            i = 0
            while i < len(strn):
                strn_i = strn[i]
                #print strn_i
                count = 0
                #print count
                #print str(i) + ':' +str(strn[i])
                while (i < len(strn)) and ( strn[i] == strn_i ):
                    count += 1
                    i += 1
                #print 'count:'+str(count)
                restr = restr + str(count) + strn_i
            return restr

        restr = '1'
        if (n != 1):
            for i in range(0,n-1):
                restr = nextnum(restr)
                #i += 1

        
        return restr

S = Solution()
print S.countAndSay(4)