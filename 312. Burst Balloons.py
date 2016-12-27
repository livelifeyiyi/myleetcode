class Solution(object):
	#not the max 
	def maxCoins1(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		def getCoins(nums, coins):
			n = len(nums)
			if n == 0:
				return coins
			if n == 3:
				i = 1
			else:
				i = nums.index(min(nums))
			print nums[i]
			numsleft = 1 if i-1 == -1 else nums[i-1]
			numsright = 1 if i+1 == n else nums[i+1]
			coins += numsleft * nums[i] * numsright
			nums.pop(i)
			coins = getCoins(nums,coins)
			return coins
		coins = 0
		return getCoins(nums,coins)
	def maxCoins(self, nums):
		nums = [1] + nums + [1]
		n = len(nums)
		dp = [[0] * n for i in range(n)]	
		def getCoins(i, j):
			#print i,j
			if dp[i][j] or j == i + 1:
				return dp[i][j]
			coins = 0
			for k in range(i+1, j):
				coins = max(coins, nums[i]*nums[k]*nums[j] + getCoins(i,k) + getCoins(k,j))
			dp[i][j] = coins
			return coins
		return getCoins(0,n-1)

S =Solution()
print S.maxCoins([3,1,5,8])