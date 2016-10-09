class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        num = len(triangle)
        if num == 1: return triangle[0][0]
        for i in range(1, num):
            for j in range(0,len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[-1])
S = Solution()
print S.minimumTotal([[1],[2,3]])