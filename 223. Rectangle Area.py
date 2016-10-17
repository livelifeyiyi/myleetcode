class Solution(object):
	def computeArea(self, A, B, C, D, E, F, G, H):
		res = (C-A) * (D-B) + (G-E) * (H-F) - max(min(C, G) - max(E, A), 0) * max(min(H, D) - max(B, F), 0)
		'''
		(C - A) * (D - B) + (G - E) * (H - F) - (sorted([A, C, E, G])[2] - sorted([A, C, E, G])[1]) * \
		(sorted([B, D, F, H])[2] - sorted([B, D, F, H])[1]) if sorted([A, C, E, G])[1] >= A and sorted([A, C, E, G])[2] <= C and \
															  sorted([B, D, F, H])[1] >= B and sorted([B, D, F, H])[2] <= D else \
			(C - A) * (D - B) + (G - E) * ( H - F)'''
		return res
S = Solution()
print S.computeArea(-3,0,3,4,0,-1,9,2)