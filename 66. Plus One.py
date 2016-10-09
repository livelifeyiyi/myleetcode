class Solution(object):
    def plusOne(self, digits):
		if digits == []:
			return []
		i = len(digits) - 1
		digits[i] += 1
		print digits[i]
		
		while  i > 0 and digits[i] >= 10 :
			digits[i] -= 10
			digits[i-1] += 1
			i -= 1
		if digits[0] >= 10:
			digits[0] -= 10
			digits.insert(0,1)
		return digits
S = Solution()
print S.plusOne([9,9,9])