class Solution(object):
	#200+ ms
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		rows = len(matrix)
		colums = len(matrix[0])
		i = 0
		while i < rows:
			l,r = 0, colums-1
			m = (l+r) / 2
			if matrix[i][m] == target or matrix[i][l] == target or matrix[i][r] == target:
				return True
			while l+1 < r:
				if matrix[i][r] < target or matrix[i][l] > target:
					break  
				if matrix[i][m] == target or matrix[i][l] == target or matrix[i][r] == target:
					return True
				if matrix[i][m] > target:
					r = m
					m = (l+r) / 2
					continue
				if matrix[i][m] < target:
					l = m
					m = (l+r) / 2
					continue
			i += 1
		return False

	#89ms
	def searchMatrix1(self, matrix, target):
		rows = len(matrix)
		colums = len(matrix[0])
		r, c = 0, colums - 1
		while 0 <= r < rows and 0 <= c < colums:
			if matrix[r][c] == target:
				return True
			if matrix[r][c] > target:
				c -= 1
			else:
				r += 1
		return False
'''matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]'''
matrix = [[-5]]
S = Solution()
print S.searchMatrix1(matrix, -10)
