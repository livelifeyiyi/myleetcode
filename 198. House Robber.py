class Solution(object):
	def rob(self, nums):
		houses = len(nums)
		if houses == 1:
			return nums[0]
		max_gap = houses - 1
		max_money, money = 0, 0
		for gap in xrange(1, max_gap+1):
			j = 0
			for i in range(0, gap+1):
				j = j + i
				while j < houses:
					money += nums[j]
					j += gap+1
				if money > max_money :
					max_money = money
				j = 0
				money = 0
		return max_money
	'''f(0) = nums[0]
	f(1) = max(num[0], num[1])
	f(k) = max( f(k-2) + nums[k], f(k-1) )'''
	def rob2(self, nums):

		last, now = 0, 0
		for i in nums:
			last, now = now, max(last + i, now)
		return now

s = Solution()
print s.rob2([4,1,2,7,5,3,1])