class Solution(object):
	def convertToTitle(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		dict = {0: '', 1: 'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N',
				15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
		num26 = []
		num = n
		k = 0
		if n <= 26:
			return dict[n]
		while num > 26:
			i = (num-1) / 26
			#num26[k] = num - 26*i
			num26.append(num - 26*i)
			k += 1
			num = i
		num26.append(num)
		lens = len(num26)
		string = ''
		for i in range(0,  lens):
			key = num26[lens-1-i]
			print key
			#string += str(dict[key])
			string += chr(ord('A') + key-1)
		return string

	def titleToNumber(self, s):
		lens = len(s)
		t, num = 0, 0
		for i in range(lens):
			j = lens - 1 -i
			num += pow(26, t) * (ord(s[j]) - ord('A') + 1)
			t += 1

		return num

S = Solution()
print S.titleToNumber('B')
#print S.convertToTitle(27)

#print ord('A')
#print unichr(ord('A')+1)