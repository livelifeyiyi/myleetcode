import pdb
class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		binary = bin(n)[2:].zfill(32)
		print binary
		print format(n, 'b').zfill(32)
		binary = binary[::-1]
		return int(binary,2)

	def hammingWeight(self, n):
		n_bac = n
		bin_n = format(n, 'b').zfill(32)
		print bin_n
		print bin_n.count('1')

		#method 2
		res = 0
		while n > 0:
			res += n % 2
			n /= 2
		print res
		#method 3, n & (n-1)
		count = 0
		while n_bac:
			n_bac = n_bac & (n_bac - 1)
			count += 1
		print count

S = Solution()
S.hammingWeight(4)