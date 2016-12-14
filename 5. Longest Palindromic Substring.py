class Solution(object):
	#too slow 
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		n = len(s)
		reverS = s[::-1]
		if s == reverS:
			return s
		maxval = 0
		res = []
		#val = ''
		mark = [[0 for i in range(n+1)] for j in range(n+1)]
		for i in range(0, n):
			for j in range(0, n):
				if s[i] == reverS[j]:
					#mark[i][j] = 1
					mark[i+1][j+1] = mark[i][j] + 1
				
					if mark[i+1][j+1] >= maxval: 
						maxval = mark[i+1][j+1]
						p = i + 1  
						subs = s[p-maxval:p]
						#print subs
						if subs == subs[::-1]:
							res.append(subs)
		#print res
		return res[-1]
	'''
	Basic thought is simple. when you increase s by 1 character, you could only increase maxPalindromeLen by 1 or 2, 
	and that new maxPalindrome includes this new character.
	Proof: if on adding 1 character, maxPalindromeLen increased by 3 or more, 
	say the new maxPalindromeLen is Q, and the old maxPalindromeLen is P, and Q>=P+3. 
	Then it would mean, even without this new checkaracter, there would be a palindromic substring ending in the last character, 
	whose length is at least Q-2. Since Q-2 would be >P, this contradicts the condition that P is the maxPalindromeLen without the additional character.

	So, it becomes simple, you only need to scan from beginning to the end, adding one character at a time, keeping track of maxPalindromeLen, and for each added character, you check if the substrings ending with this new character, with length P+1 or P+2, are palindromes, and update accordingly.
	'''
	def longestPalindrome2(self, s):
		if len(s)==0:
			return 0
		maxLen=1
		start=0
		for i in xrange(len(s)):
			print i,maxLen, s[i-maxLen-1:i+1]
			if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
				start=i-maxLen-1
				maxLen+=2
				continue
			if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
				start=i-maxLen
				maxLen+=1
		return s[start:start+maxLen]
s = Solution()
testdata = 'dababab'
#testdata = "esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq"
print s.longestPalindrome2(testdata)
