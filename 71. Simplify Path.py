class Solution(object):
	def simplifyPath(self, path):
		"""
		:type path: str
		:rtype: str
		"""
		listpath = [p for p in path.split('/') if p != '.' and p != '']
		
		res = []
		print listpath
		for p in listpath:
			if p == '..':
				if res:
					res.pop()
			else: res.append(p)
		print res
		return '/' + '/'.join(res)
		
S = Solution()
print S.simplifyPath("/abc/...")
