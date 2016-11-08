from collections import defaultdict
class Solution(object):
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		table = defaultdict(list)
		for string in strs:
			sortstr = "".join(sorted(string))
			if sortstr not in table:
				table[sortstr] = []
			table[sortstr].append(string)
		return table.values()
s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

