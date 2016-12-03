class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		n = len(height)
		water = width = 0
		#stack = []
		if n <= 2:
			return 0
		if min(height[0], height[-1]) >= max(height[1:n-1]):
			return min(height[0], height[-1])*(n-2)-sum(height[1:n-1])
		i = 1
		j = 0
		while i < n:
			#stack.append(height[i])
			if height[i] <= height[i-1]:
				i += 1
				continue
			if height[i] > height[i-1]:
				'''
				j = len(stack)-1
				while j > 0 and stack[j] <= height[i+1]:
					diff_high = height[i+1] - stack[j]
					width = 1
					if stack[j -1] == stack[j]:
						width += 1 
						j -= 1
					j -= 1'''
				#if j <= 1 or (j != i and height[j] > height[j-1]):
				if j == 0 or(j != i and height[j] > height[j - 1]):
					j = i-1
					width = 0
				high_right = height[i] - height[j]
				right = height[i]
				width += 1
				#while j == 0 or (j > 0 and height[j] < height[j-1]):
				while j and height[j] < height[j - 1]:
					high_left = height[j-1] - height[j]
					if high_left == 0:
						width += 1
						j -= 1
						continue
					water += min(high_left, high_right) * width
					j -= 1
					width += 1
					if height[j-1] <= right: continue
					else: break
				i += 1
				#width += 1
		return water

	def getvalue(self, height):
		n = len(height)

		if max(height) == height[0]:
			height.pop(0)
		while n >2 and min(height) == height[-1]:
			height.pop()
			n -= 1
		if n <= 2:
			return 0
		if min(height[0], height[-1]) >= max(height[1:n - 1]):
			return min(height[0], height[-1]) * (n - 2) - sum(height[1:n - 1])
		else: return None
	#253/315
	def trap2(self, height):
		n = len(height)
		if n <= 2:
			return 0
		water = 0
		i = j = 0
		while j >= 0 and j < n-1:
			while i < n-1 and height[i] == height[i+1]:
				i += 1
			j = i+1
			if j > n-1: break
			while j < n-1 and height[j] < height[i]:
				j += 1
			'''p = j
			while height[p-1] > height[p]:
				p -= 1'''
			new = height[i:j+1]
			value = self.getvalue(new)
			if value != None:
				water += value
				i = j
				continue
			else:
				i += 1
				j = i
				#if new: water += self.getvalue(new.reverse())
				continue
		return water
	def trap3(self, height):
		l = 0
		r = len(height) - 1
		lmax = rmax = water = 0
		while l <= r:
			lmax = max(lmax, height[l])
			rmax = max(rmax, height[r])
			if lmax < rmax:
				water += lmax - height[l]
				l += 1
			else:
				water += rmax - height[r]
				r -= 1
		return water


testSet = [[9,6,8,8,5,6,3],[4,3,3,9,3,0,9,2,8,3],[4,9,4,5,3,2],[5,4,1,2],[5,5,1,7,1,1,5,2,7,6],[4,2,0,3,2,4,3,4],[5,2,1,2,1,5],[4,2,3], [2,1,0,2], [0,1,0,2,1,0,1,3,2,1,2,1]]
s = Solution()
for i in testSet:
	print s.trap2(i)
	#[4,3,3,9,3,0,9,2,8,3])  23
	#[4,9,4,5,3,2])
	#[5,4,1,2])	#1
	#[5,5,1,7,1,1,5,2,7,6])	#23
	#[4,2,0,3,2,4,3,4])	#10
	#[5,2,1,2,1,5])	#14
	#[4,2,3])	#1
	#[2,1,0,2])	#3
	#[0,1,0,2,1,0,1,3,2,1,2,1])	#6
