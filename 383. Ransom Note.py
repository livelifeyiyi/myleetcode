import collections
class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		"""
		:type ransomNote: str
		:type magazine: str
		:rtype: bool
		"""
		#return not collections.Counter(ransomNote) - collections.Counter(magazine)
		if ransomNote == magazine:
			return True
		need = collections.Counter(ransomNote)
		missing = len(ransomNote)
		for i in magazine:
			missing -= need[i] > 0
			need[i] -= 1
			if missing == 0:
				return True
		return False
s = Solution()
print s.canConstruct('aabc','aab')


