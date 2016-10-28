class Solution(object):
	def getHint(self, secret, guess):
		"""
		:type secret: str
		:type guess: str
		:rtype: str
		"""
		bulls, cows, mark = 0, 0, [0]*10
		for i in range(len(secret)):
			if secret[i] == guess[i]:
				#bulls.append(secret[i])
				bulls += 1
			else:
				mark[int(secret[i])] += 1
		for i in range(len(secret)):
			if (secret[i] != guess[i]) and mark[int(guess[i])] > 0:
				#cows.append(secret[i])
				cows += 1
				mark[int(guess[i])] -= 1
		return str(bulls) + 'A' + str(cows) + 'B'
s = Solution()
print s.getHint('11234', '01115')