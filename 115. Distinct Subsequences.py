class Solution(object):	
	####wrong
	def numDistinct(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: int
		"""
		res = []
		#dic.fromkeys(t,0)
		if s == t: return 0
		diff = len(s) - len(t)
		sumnum = 0
		if diff == 1:
			for i in range(len(s)):
				val = s[:i] + s[i+1:]
				if val == t:
					print i
					res.append(val)
			sumnum = len(res)
		else:
			i = j = counts = countt = 0
			val = ''
			while i < len(s) and j < len(t):
				while i < len(s) and s[i] == t[j]:
					i += 1
					#dic[s[i]] += 1
					counts += 1
				while j < len(t) and t[j] == s[i-1]:
					j += 1
					countt += 1
				divider = divided = 1
				for x1 in range(0,countt):
					divider *= counts
					counts -= 1
					divided *= countt
					countt -= 1
				sumnum += divider / divided
				if s[i] != t[j]:
					i += 1
			if i == len(s) -1 and j == len(t)-1:
				sumnum += 1
		#print res
		return sumnum
	def numDistinct2(self, s, t):
		'''
		idea:
		the first row must be filled with 1. That's because the empty string is a subsequence of any string but only 1 time.
		the first column of every rows except the first must be 0. This is because an empty string cannot contain a non-empty string as a substring.
		for each (x, y), we check if S[x] == T[y] we add the previous item and the previous item in the previous row, 
		otherwise we copy the previous item in the same row. 
		'''
		ls, lt = len(s)+1, len(t)+1
		dp = [[0 for i in range(ls)] for j in range(lt)]
		#dp = [[1] * lt for _ in xrange(ls)]
		for i in range(ls):
			dp[0][i] = 1
		#print dp
		for i in range(1,lt):
			for j in range(1,ls):
				dp[i][j] = dp[i][j-1] + dp[i-1][j-1] *(s[j-1] == t[i-1])
		#print dp
		return dp[-1][-1]
S =Solution()
print S.numDistinct2('rabbbit','rabbit')
	#'abcde','ace')
	#'rabbbit','rabbit')