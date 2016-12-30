# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
	def guessNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		def guess(num, input = 6):
			if num < input: return 1
			if num > input: return -1
			else: return 0

		begin, end = 1, n
		mid = (begin + end) / 2
		while begin < end-1:
			if guess(mid) == 1:
				begin = mid 
				mid = (begin + end) / 2
				continue
			if guess(mid) == -1:
				end = mid 
				mid = (begin + end) / 2
				continue
			if guess(mid) == 0: return mid
		return begin if guess(begin) == 0 else end
S =Solution()
print S.guessNumber(10)