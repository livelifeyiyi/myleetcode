from Levenshtein import *
class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		n, m = len(word1), len(word2) 
		if n == 0: return m
		if m == 0: return n
		edit = [[0 for i in range(0, n+1)] for j in range(0, m+1)]
		for i in range(0, n+1):
			edit[0][i] = i
		for j in range(0,m+1):
			edit[j][0] = j
		#print edit
		for i in range(1, n+1):
			for j in range(1,m+1):
				temp = 0 if word1[i-1] == word2[j-1] else 1
				edit[j][i] = min(edit[j-1][i]+1, edit[j][i-1]+1, edit[j-1][i-1]+temp)
		#print edit
		return edit[m][n]

s = Solution()
str1, str2 = 'a', 'ab'
print s.minDistance(str1,str2)

print distance(str1,str2)