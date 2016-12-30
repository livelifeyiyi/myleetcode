# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):	
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		begin = 1
		end = n
		mid = (begin + end) / 2
		while begin < end-1:
			if not isBadVersion(mid):
				begin, mid = mid, (begin + end) / 2
				continue
			if isBadVersion(mid):
				end, mid = mid, (begin + end) / 2
				continue
		return begin if isBadVersion(begin) else end
