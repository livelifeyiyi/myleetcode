class Solution(object):
	def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		vowel = ['a', 'e', 'u', 'i','o','A', 'E', 'U', 'I','O']
		l = list(s)
		n = len(s)
		left, right = 0, n -1
		while left < right:
			if l[left] not in vowel and l[right] not in vowel:
				left += 1
				right -= 1
				continue
			if l[left] in vowel and l[right] not in vowel:
				right -= 1
				continue
			if l[right] in vowel and l[left] not in vowel:
				left += 1
				continue
			l[left], l[right] = l[right], l[left]
			left += 1
			right -= 1
		return "".join(l)

s = Solution()
print s.reverseVowels2('hello')



