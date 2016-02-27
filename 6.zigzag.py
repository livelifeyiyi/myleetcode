# -*- coding: utf-8 -*- 
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr = []
        arr = s[:]
        #字符串长度
        lennum = len(s)
        #考虑一行的情况
        if numRows <= 1:
            return s
        else:
            #每组数目
            perzunum = 2 * numRows - 2
            #总共几组
            zunum = lennum // perzunum + 1
            yu = lennum % perzunum
            rearr = [[] for i in range(numRows)]
            n = 0
            
            
            for i in range(0,zunum):
                n = perzunum * i
                #第1行
                if (n < lennum):
                    rearr[0].append(arr[n])
            for i in range(0,zunum):
                n = perzunum * i + numRows - 1
                #最后1行
                if (n < lennum):
                    rearr[numRows-1].append(arr[n])
            #中间行
            for j in range(1,numRows-1):
                n = perzunum * 0 + j
                if (n < lennum):
                    rearr[j].append(arr[n])
                #zunum+1而不是zunum：考虑不完全一组的情况，比如ABCDE按4组拍。
                for i in range(1,zunum+1):
                    n = perzunum * i - j
                    if (n < lennum):
                        rearr[j].append(arr[n])
                    n = perzunum * i + j
                    if (n < lennum):
                        rearr[j].append(arr[n])
            restr = ''
            for i in range(0,numRows):
                restr1 = ''.join(rearr[i])
                restr = restr + restr1

            #restr1 = ''.join(rearr[0])
            #restr2 = ''.join(rearr[1])
            #restr = restr1 +restr2
            return restr
S = Solution()                    
print S.convert("ABCDE", 4)             
                
        