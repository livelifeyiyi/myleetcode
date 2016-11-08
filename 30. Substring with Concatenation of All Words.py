from collections import Counter
class Solution(object):
	#did not consider the duplicate data
	def findSubstring(self, s, words):
		"""
		:type s: str
		:type words: List[str]
		:rtype: List[int]
		"""
		res = []
		if not s or not words: return res
		words_len = len(words[0])
		words_num = len(words)
		table = dict.fromkeys(words, 0)
		i = 0
		while i < len(s)-words_len+1:
			str = s[i:words_len+i]
			if str not in words:
				i = words_len + i
				for key in table.keys():
					if table[key] > 0: table[key] -= 1
				continue
			if str in words:
				if table[str] == 1:
					table[str] -= 1
				table[str] += 1
			i = words_len + i
			if sum(table.values()) == words_num:
				beginindex = i - words_len*words_num
				res.append(beginindex)
				str2 = s[beginindex:words_len+beginindex]
				table[str2] -= 1
		return res
			#if str in dict.keys(): dict[str].append(i)
		'''value = 0
		while value <= len(res)-words_num:
			for i in range(1,words_num):
				if res[value] + words_len != res[value+i]:
					continue
			res2.append(res[value])
			value += words_num
		return res2
		#index = zip(dict[i] for i in dict.keys())'''

	def findSubstring2(self, s, words):
		res = []
		if not s or not words: return res
		words_len = len(words[0])
		words_num = len(words)
		for index in range(0, words_len):
			to_match = len(words)
			table = Counter(words)
			i = index
			while i < len(s)-words_len+1:
				str = s[i:words_len+i]
				'''TLE
				if str not in words:
					i = words_len + i
					to_match = len(words)
					table = Counter(words)
					continue
				else:'''
				if str in table:
					table[str] -= 1
					to_match -= 1
					if table[str] == 0:
						del table[str]
					if to_match == 0:
						beginindex = i - words_len * (words_num - 1)
						res.append(beginindex)
						'''str2 = s[beginindex:words_len + beginindex]
						table[str2] += 1
						to_match += 1'''
					i = words_len + i
					#continue
				#if str not in table:
				elif to_match != words_num:
					beginindex = i - words_len * (words_num - to_match)
					str2 = s[beginindex:words_len + beginindex]
					table[str2] += 1
					to_match += 1
				else:i = words_len + i
		return res
s = Solution()
print s.findSubstring2("wordgoodgoodgoodbestword",["word","good","best","good"])
	#"abababab",["a","b","a"])
	#"aaaaaaaa",["aa","aa","aa"])
	#"lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"])
	#"barfoofoobarthefoobarman", ["bar","foo","the"])
	#"barfoothefoobarman", ["foo", "bar"])
	#"wordgoodgoodgoodbestword",["word","good","best","good"])