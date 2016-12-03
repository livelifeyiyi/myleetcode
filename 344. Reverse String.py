class Solution(object):
	def reverseString1(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		return s[::-1]
	# two points
	def reverseString2(self, s):
		
		n = len(s)
		print s[n/2:] + "aaaa"+ s[:n/2]
		list_s = list(s)
		left, right = 0, n - 1
		while left < right:
			list_s[left], list_s[right] = list_s[right], list_s[left]
			left += 1
			right -= 1
		return "".join(list_s)
	def reverseString3(self, s):
		n = len(s)
		if n < 2:
			return s
		return self.reverseString3(s[n/2:]) + self.reverseString3(s[:n/2])
	def reverseString_TLE(self, s):
		res = ''
		n = len(s)
		while n:
			res += s[n-1]
			n -= 1
		return res
s = Solution()
print s.reverseString3('hello')