class Solution(object):
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		n = len(s)
		res = []
		tmp = []
		num = []
		if n < 4:
			return res
		if n == 12:
			num.append([3,3,3,3])
		else:
			for a in range(1,4):
				for b in range(1,4):
					for c in range(1,4):
						for d in range(1,4):
							if a + b + c + d == n:
								val = [a,b,c,d]
								num.append(val)
		print num
		for i in range(len(num)):
			m = 0
			for k in num[i]:
				n = m + k
				print m,n
				val = s[m:n]
				m = n
				intv = int(val)
				print val, intv,len(str(intv))
				if val and (len(str(intv)) != len(val) or intv < 0 or intv > 255):
					tmp = []
					break
				tmp.append(val)
			if tmp:
				res.append('.'.join(tmp))
				tmp = []
			'''
				vala = s[0:a]
				valb = s[a:a+b]
				valc = s[a+b:a+b+c]
				vald = s[a+b+c:a+b+c+d]'''
		return res

S = Solution()
print S.restoreIpAddresses("255255255255") 