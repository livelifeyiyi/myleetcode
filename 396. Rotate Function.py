class Solution(object):
	#TLE
	def maxRotateFunction(self, A):
		"""
        :type A: List[int]
        :rtype: int
        """
		#result = []
		max = self.calFunction(A)
		for i in range(0, len(A)-1):
			#result.append(self.calFunction(A))
			val = A.pop()
			A.insert(0, val)
			currval = self.calFunction(A)
			if currval > max: max = currval
		return max
		#return max(result) if result else 0
	def calFunction(self, A):
		sumval = 0
		for i in range(0, len(A)):
			sumval += i * A[i]
		return sumval

	def maxRotateFunction2(self, A):
		max = self.calFunction(A)
		sumA = sum(A)
		n = len(A)
		Fi = max
		for i in range(1, n):
			Fi = Fi + sumA - n * A[n-i]
			if Fi > max: max = Fi
		return max
s = Solution()
print s.maxRotateFunction2([4, 3, 2, 6])