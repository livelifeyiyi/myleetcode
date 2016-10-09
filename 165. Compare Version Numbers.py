class Solution(object):
	def compareVersion(self, version1, version2):
		"""
		:type version1: str
		:type version2: str
		:rtype: int
		"""
		v1 = version1.split('.')
		v2 = version2.split('.')
		while v1 and v2:
			if int(v1[0]) > int(v2[0]):
				return 1
			elif int(v1[0]) < int(v2[0]):
				return -1
			else:
				v1.pop(0)
				v2.pop(0)
				continue
		if not v1 and not v2:
			return 0
		elif sum(map(int, v1+v2)) == 0: return 0
		elif len(v1) > len(v2): return 1
		elif len(v1) < len(v2): return -1
		else: return 0


S = Solution()
print S.compareVersion("1.0.1","1.0.1.2")