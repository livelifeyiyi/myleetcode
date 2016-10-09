
class Solution(object):
    def generate_1st(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        triangle = [[] for i in range(numRows)]
        triangle[0] = [1]
        if numRows == 1:
            return [[1]]
        for i in range(1, numRows):
            n = i +1
            triangle[i] = [0 for j in range(n)]
            triangle[i][0] = 1
            triangle[i][i] = 1
            for k in range(1,i):
                triangle[i][k] = triangle[i-1][k-1] + triangle[i-1][k]
        return triangle
    def generate_2nd(self, rowIndex):
        if rowIndex == 0:return [1]
        row = [1,1]
        k = [0]
        result = [row]
        for i in range(1, rowIndex):
            row = [l+r for l,r in zip(row+k, k+row)]
            #result.append(row)
        return row
S = Solution()
print S.generate_2nd(4)       