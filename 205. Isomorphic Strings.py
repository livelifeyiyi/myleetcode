class Solution(object):
	def isIsomorphic(self, s, t):
		if not s and not t: return True
		#if not s or not t: return False
		s_num = [s[0]]
		t_num = [t[0]]
		s2 = ''
		t2 = ''
		for i in range(len(s)):
			if s[i] not in s_num:
				s_num.append(s[i])
			s2 += str(s_num.index(s[i]))
		for j in range(len(t)):
			if t[j] not in t_num:
				t_num.append(t[j])
			t2 += str(t_num.index(t[j]))
		return s2 == t2
	def isIsomorphic2(self, s, t):
		return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
S = Solution()
print S.isIsomorphic2('aba', 'baa')