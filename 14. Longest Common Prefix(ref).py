class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lens = len(strs)
        if lens == 0 :
            return ""
        n = lens-1
        if n == 0:
            return strs[0]
        num,m = 0,0
        while n >0:
            num += n
            n = n-1
        restr = [ '' for i in range(num)]
        for i in range(0,lens-1):
            for j in range(i+1,lens):
                
                stri = strs[i]
                strj = strs[j]
                lenij = len(stri) if len(stri)<len(strj) else len(strj)
                if lenij == 0 :
                    return ""
                for k in range(0,lenij):
                    if stri[k] == strj[k]:
                        if m <num:
                            restr[m] += stri[k]
                    else:
                        break
                m += 1        
        #print restr
        if num == 1:
            return restr[0]
        for i in range(0,lens-1):
            if len(restr[i]) > len(restr[i+1]):
                a = restr[i]
                restr[i] = restr[i+1]
                restr[i+1] = a
            else:
                return ""
        restring = restr[lens-1]
        return restring

class Solutionref(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ''
        len_prefix = 0
        max_prefix = ''
        isStoped = False
        while len(strs[0]) > len_prefix:
            char = strs[0][len_prefix]
            for i in xrange(1,len(strs)):
                if (len(strs[i]) <= len_prefix) or (strs[i][len_prefix] != char):
                    isStoped = True
                    break
            if isStoped:
                break
            else:
                len_prefix += 1
                max_prefix += char
        return max_prefix

S = Solutionref()
print S.longestCommonPrefix(['testtt','test1'])
