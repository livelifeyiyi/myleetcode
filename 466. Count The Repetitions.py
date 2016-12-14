class Solution(object):
	def getMaxRepetitions(self, s1, n1, s2, n2):
		"""
		:type s1: str
		:type n1: int
		:type s2: str
		:type n2: int
		:rtype: int
		"""
		if s1 == s2:
			return n1/n2
		if len(s1) * n1 < len(s2) * n2:
			return 0
		num = self.isObtained(s2, s1)
		if num:
			return n1 / n2 * num
		S1 = self.connectStrings(s1, n1)
		S2 = self.connectStrings(s2, n2)
		M = len(S1) / len(S2)
		while M:
			SS2 = self.connectStrings(S2, M)
			if len(SS2) > len(S1) or (len(SS2) == len(S1) and SS2 != S1):
				M -= 1
				continue
			if self.isObtained(SS2, S1):
				return M
			M -= 1
		return M

	def connectStrings(self, s, n):
		res = ''
		for i in range(0, n):
			res += s
		return res
	def isObtained(self, substring, string):
		l = list(string)
		#l.sort()
		l_sub = list(substring)
		#l_sub.sort()
		lenl = len(l)
		i = 0
		#for i in range(0, lenl):
		while i < lenl:
			if l[i] not in l_sub:
				l.pop(i)
				i -= 1
				lenl -= 1
			i += 1
		if l == l_sub: return 1
		num = count = 0
		while num + len(l_sub) < len(l):
			if l[num:num+len(l_sub)] == l_sub:
				count += 1
			num += 1
		'''for j in range(0, len(l_sub)):
			if l[j] != l_sub[j]:
				return 0'''
		return count
s = Solution()
print s.getMaxRepetitions('lovelivenanjomusicforever', 100000, 'nanjo', 10)
'''
"lovelivenanjomusicforever"
100000
"nanjo"
10

lovenicoloveliveniconiconiconiniconjcoaaajo'''