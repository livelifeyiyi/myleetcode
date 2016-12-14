class Solution(object):
	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		n = len(s)
		stack = []
		num = maxnum = 0
		for i in range(n):
			#print stack
			if s[i] ==')' and stack and s[stack[-1]] == '(':
				stack.pop()
				num += 1
				'''if stack.count('(') == 0:
					maxnum = max(num*2, maxnum)
					num = 0'''
			else:
				stack.append(i)
			print stack
		if not stack:
			maxnum = num*2
		else:
			a, b = n, 0
			while stack:
				b = stack[-1]
				stack.pop()
				maxnum = max(maxnum, a - b -1)
				a = b
			#####to avoid the case that stack has the only one at the end of the str s
			maxnum = max(maxnum, a)
		return maxnum
S = Solution()
print S.longestValidParentheses('()())')