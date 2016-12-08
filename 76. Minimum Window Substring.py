import collections
class Solution(object):
	#TLE
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		n = len(s)
		if len(t) > n:
			return ""
		min_len = n + 1
		left = right = 0
		resstr = ""
		while right < n:
			while left <= right and s[left] not in t:
				left += 1
			substr = s[left:right+1]
			substr_bak = list(substr)
			#for i in range(len(t)):
			i = 0
			while i < len(t):
				if t[i] in substr_bak:
					substr_bak.pop(substr_bak.index(t[i]))
					i += 1
					continue
				if t[i] not in substr_bak:
					break
				#i += 1
			if i == len(t):
				#min_len = min(min_len, len(substr))
				if len(substr) < min_len:
					min_len = len(substr)
					resstr = substr
				left += 1
				continue
			right += 1
		return resstr

	def minWindow2(self, s, t):
		need, missing = collections.Counter(t), len(t)
		i = I = J = 0
		for j, c in enumerate(s, 1):
			missing -= need[c] > 0
			need[c] -= 1
			if not missing:
				while i < j and need[s[i]] < 0:
					need[s[i]] += 1
					i += 1
				if not J or j - i <= J - I:
					I, J = i, j
		return s[I:J]
s = Solution()
print s.minWindow("cabwefgewcwaefgcf","cae")
	#"bba", "ab")
	#"aa", "aa")
	#"ADOBECODEBANC", "ABC")
	#"ab","a")

