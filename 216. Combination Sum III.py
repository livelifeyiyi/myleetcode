#-*- coding: utf-8 -*-
class Solution(object):
	#k个数和为n
	def combinationSum3(self, k, n):
		num = [1,2,3,4,5,6,7,8,9]
		if n > sum(num):
			return []
		result = []
		self.sum_arr(k, n, 1, [], result)
		return result
	def sum_arr(self, k, n, curr, arr, result):
		if len(arr) == k:
			if sum(arr) == n:
				#result.append(arr)
				result.append(list(arr))
			return
		if sum(arr) > n or len(arr) > k:
			return
		for i in range(curr, 10):
			arr.append(i)
			self.sum_arr(k, n, i+1, arr, result)
			arr.pop()

S = Solution()
print S.combinationSum3(3, 7)