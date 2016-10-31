from collections import Counter
class Solution(object):
	def findAnagrams(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: List[int]
		"""
		lens = len(s)
		lenp = len(p)
		i = 0
		res = []
		if lens < lenp: return res
		while i + lenp - 1 < lens:
			parts = s[i:i+lenp]
			#if setp == set(parts) and lenp == len(parts):
			if Counter(p) == Counter(parts):
				res.append(i)
			i += 1
		return res
	def findAnagrams2(self, s, p):
		lens = len(s)
		lenp = len(p)
		pcounter = Counter(p)
		scounter = Counter(s[:lenp-1])
		res = []
		if lens < lenp: return res
		for i in range(lenp - 1 , lens):
			scounter[s[i]] += 1
			if pcounter == scounter:
				res.append(i-lenp+1)
			scounter[s[i-lenp+1]] -= 1
			if scounter[s[i-lenp+1]] == 0:
				del scounter[s[i-lenp+1]]
		return res
s = Solution()
print s.findAnagrams2('abab', 'ab')




