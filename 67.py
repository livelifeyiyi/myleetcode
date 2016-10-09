#	67	Add Binary
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        #print i,j
        if i > j:
        	b = '0' * (i-j) + b
        	j = i
        elif i < j:
        	a = '0' * (j-i) + a
        	i = j
        #print a,b
        plus = 0
        reverse_add =''
        re_add =''
        while i >=0 and j >= 0:
        	add = int(a[i]) + int(b[j]) + plus 
        	if add >= 2:
        		add -= 2
        		plus = 1
        	else:plus = 0
        	reverse_add += str(add)
        	if i == j == 0:
        		if plus == 1:
        			reverse_add += '1'
        	add = 0	
        	i -= 1
        	j -= 1
        t = len(reverse_add) - 1
        while t >= 0:
        	re_add += reverse_add[t]
        	t -= 1
        return re_add
S = Solution()
print S.addBinary('1010','1011')