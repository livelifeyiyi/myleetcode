class Solution(object):
	def validIPAddress(self, IP):
		"""
		:type IP: str
		:rtype: str
		"""
		
		def ipv4(IP):
			ip = [i for i in IP.split('.')] # if i !=''
			if len(ip) != 4: # or IP.count('.') != len(ip) - 1:
				return "Neither"
			for j in ip:
				if j == '': return "Neither"
				try:
					intj = int(j)
				except ValueError:
					return "Neither"
				#invalid leading 0, invalid number
				if len(str(intj)) != len(j) or intj < 0 or intj >255:
					return "Neither"
			return 'IPv4'
		def ipv6(IP):
			ip = [i for i in IP.split(':')] # if i != ''
			#replace a consecutive group of zero value with a single empty group using two consecutive colons (::) 
			if len(ip) != 8:
				return "Neither"
			for j in ip:
				if j == '' or j[0] == '-': return "Neither"
				try:
					intval = int(j, 16)
				except ValueError:
					return "Neither"
				if len(j) > 4 or (intval > pow(16,4)) or intval < 0:
					return "Neither"
			return 'IPv6'
		n = len(IP)
		if n > 12:
			return ipv6(IP)
		else:
			return ipv4(IP)

S = Solution()
print S.validIPAddress("1081:db8:85a3:01:-0:8A2E:0370:7334")

